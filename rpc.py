import json
import utils
from lsp.types import ResponseMessage


def encode(msg: ResponseMessage) -> str:
    json_msg = json.dumps(utils.to_dict(msg))
    return f'Content-Length: {len(json_msg)}\r\n\r\n{json_msg}'


def decode(msg: str):
    header, content = msg.split('\r\n\r\n')
    return header, content
