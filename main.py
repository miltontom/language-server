import sys
import logging
import json
import os
from types import SimpleNamespace

import rpc
from lsp.types import (
    InitializeResult,
    ServerInfo,
    ResponseMessage,
    ServerCapabilities,
    TextDocumentItem
)


EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def setup_logging():
    log_dir = os.path.join(os.getenv('localappdata'), 'ToyLanguageServer', 'Log')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(filename=os.path.join(log_dir, 'server.log'),
                        filemode='a',
                        level=logging.DEBUG,
                        datefmt='%d-%m-%Y %H:%M:%S',
                        format='%(asctime)s,%(msecs)03d %(levelname)-8s %(message)s')


def send_response(response: ResponseMessage):
    rpc_message = rpc.encode(response)
    sys.stdout.buffer.write(rpc_message.encode())
    sys.stdout.buffer.flush()
    logging.info(f'Sent response')


def handle_message(message):
    msg = json.loads(message, object_hook=lambda d: SimpleNamespace(**d))
    method = msg.method

    if is_notification(msg):
        logging.debug(f'Received notification: "{method}"')
    else:
        logging.debug(f'Received request: "{method}"')

    if method == 'initialize':
        '''
        The handshake between the server and neovim is successful only
        if Neovim sents a notification with method "initialized", i.e
        a response message should be sent to Neovim announcing server
        server capabilities when Neovim sents the first request with
        method "initialize".
        '''
        client_name = msg.params.clientInfo.name
        client_version = msg.params.clientInfo.version
        logging.info(f'Connecting to client: {client_name} {client_version}')

        initialize_response = InitializeResult(
            capabilities=ServerCapabilities(
                # Document is synced by always sending the full content
                textDocumentSync=1
            ),
            serverInfo=ServerInfo('toy-language-server', '0.1.0')
        )
        response = ResponseMessage(msg.id, initialize_response)
        send_response(response)

    elif method == 'initialized':
        logging.info(f'Connection established: "{method}"')

    elif method == 'textDocument/didOpen':
        obj = TextDocumentItem(**vars(msg.params.textDocument))
        logging.info(f'Opened: {obj.uri}')

    elif method == 'shutdown':
        pass

    elif method == 'exit':
        pass


def read_message():
    header = ''
    bytes_to_read = -1
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        header = line
    bytes_to_read = int(header[len('Content-Length: '):])
    message = header + '\r\n\r\n' + sys.stdin.read(bytes_to_read)
    return message


def is_notification(message) -> bool:
    return not hasattr(message, 'id')
    

def main():
    setup_logging()

    logging.info('Server logging initiated')
    while True:
        message = read_message()
        json_content = rpc.decode(message)[1]
        handle_message(json_content)
        

main()