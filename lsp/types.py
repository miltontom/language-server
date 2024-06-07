from dataclasses import dataclass
from typing import Union, Optional, List, Dict


@dataclass(kw_only=True)
class Message:
    jsonrpc: str = '2.0'

@dataclass
class RequestMessage(Message):
    id: Union[int, str]
    method: str
    params: Optional[Union[List, Dict]] = None

@dataclass
class ResponseError:
    code: int
    message: str
    data: Optional[Union[str, int, bool, List, Dict]] = None

@dataclass
class ResponseMessage(Message):
    id: Optional[Union[int, str]]
    result: Optional[Union[str, int, bool, List, Dict]] = None
    error: Optional[ResponseError] = None
    
@dataclass
class NotificationMessage:
    method: str
    params: Optional[Union[List, Dict]] = None

@dataclass
class ServerInfo:
    name: str
    version: Optional[str] = None

@dataclass
class ServerCapabilities:
    textDocumentSync: Optional[int] = 0 # Type: TextDocumentSyncKind

@dataclass
class InitializeResult:
    capabilities: ServerCapabilities
    serverInfo: Optional[ServerInfo]

@dataclass
class TextDocumentItem:
    uri: str
    languageId: str
    version: int
    text: str # content of the file