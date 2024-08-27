from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilePath(_message.Message):
    __slots__ = ("ip", "port", "path")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: str
    path: str
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class FileChunk(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: FilePath
    def __init__(self, file_path: _Optional[_Union[FilePath, _Mapping]] = ...) -> None: ...

class ReportCompletionRequest(_message.Message):
    __slots__ = ("job_id", "file_paths")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    file_paths: _containers.RepeatedCompositeFieldContainer[FilePath]
    def __init__(self, job_id: _Optional[str] = ..., file_paths: _Optional[_Iterable[_Union[FilePath, _Mapping]]] = ...) -> None: ...

class ReportCompletionResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
