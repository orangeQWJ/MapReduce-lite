from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    M: _ClassVar[TaskType]
    R: _ClassVar[TaskType]
M: TaskType
R: TaskType

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

class JustDoItRquest(_message.Message):
    __slots__ = ("job_id", "task_type", "task_id", "python_file_path", "file_paths")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PYTHON_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    task_type: TaskType
    task_id: int
    python_file_path: FilePath
    file_paths: _containers.RepeatedCompositeFieldContainer[FilePath]
    def __init__(self, job_id: _Optional[str] = ..., task_type: _Optional[_Union[TaskType, str]] = ..., task_id: _Optional[int] = ..., python_file_path: _Optional[_Union[FilePath, _Mapping]] = ..., file_paths: _Optional[_Iterable[_Union[FilePath, _Mapping]]] = ...) -> None: ...

class JustDoItResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
