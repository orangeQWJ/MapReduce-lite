from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerAddress(_message.Message):
    __slots__ = ("ip", "port")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class FilePath(_message.Message):
    __slots__ = ("serverAddress", "path")
    SERVERADDRESS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    serverAddress: ServerAddress
    path: str
    def __init__(self, serverAddress: _Optional[_Union[ServerAddress, _Mapping]] = ..., path: _Optional[str] = ...) -> None: ...

class FileChunk(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("filePath",)
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    filePath: FilePath
    def __init__(self, filePath: _Optional[_Union[FilePath, _Mapping]] = ...) -> None: ...

class ReportCompletionRequest(_message.Message):
    __slots__ = ("jobID", "filePaths")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    FILEPATHS_FIELD_NUMBER: _ClassVar[int]
    jobID: str
    filePaths: _containers.RepeatedCompositeFieldContainer[FilePath]
    def __init__(self, jobID: _Optional[str] = ..., filePaths: _Optional[_Iterable[_Union[FilePath, _Mapping]]] = ...) -> None: ...

class ReportCompletionResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
