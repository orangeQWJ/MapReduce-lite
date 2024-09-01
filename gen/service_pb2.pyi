from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAP: _ClassVar[TaskType]
    REDUCE: _ClassVar[TaskType]
MAP: TaskType
REDUCE: TaskType

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

class RegisterWorkerRequest(_message.Message):
    __slots__ = ("server_add",)
    SERVER_ADD_FIELD_NUMBER: _ClassVar[int]
    server_add: ServerAddress
    def __init__(self, server_add: _Optional[_Union[ServerAddress, _Mapping]] = ...) -> None: ...

class RegisterWorkerResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ReportTaskRequest(_message.Message):
    __slots__ = ("jobID", "taskType", "taskID", "filePaths")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKTYPE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    FILEPATHS_FIELD_NUMBER: _ClassVar[int]
    jobID: str
    taskType: TaskType
    taskID: int
    filePaths: _containers.RepeatedCompositeFieldContainer[FilePath]
    def __init__(self, jobID: _Optional[str] = ..., taskType: _Optional[_Union[TaskType, str]] = ..., taskID: _Optional[int] = ..., filePaths: _Optional[_Iterable[_Union[FilePath, _Mapping]]] = ...) -> None: ...

class ReportTaskResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class UploadTaskRequest(_message.Message):
    __slots__ = ("mapNum", "reduceNum", "serverAddress", "mapReduceFuncPath", "filePaths")
    MAPNUM_FIELD_NUMBER: _ClassVar[int]
    REDUCENUM_FIELD_NUMBER: _ClassVar[int]
    SERVERADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAPREDUCEFUNCPATH_FIELD_NUMBER: _ClassVar[int]
    FILEPATHS_FIELD_NUMBER: _ClassVar[int]
    mapNum: int
    reduceNum: int
    serverAddress: ServerAddress
    mapReduceFuncPath: FilePath
    filePaths: _containers.RepeatedCompositeFieldContainer[FilePath]
    def __init__(self, mapNum: _Optional[int] = ..., reduceNum: _Optional[int] = ..., serverAddress: _Optional[_Union[ServerAddress, _Mapping]] = ..., mapReduceFuncPath: _Optional[_Union[FilePath, _Mapping]] = ..., filePaths: _Optional[_Iterable[_Union[FilePath, _Mapping]]] = ...) -> None: ...

class UploadTaskResponse(_message.Message):
    __slots__ = ("jobID", "success")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    jobID: str
    success: bool
    def __init__(self, jobID: _Optional[str] = ..., success: bool = ...) -> None: ...

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

class JustDoItRequest(_message.Message):
    __slots__ = ("jobID", "taskType", "taskID", "mapReduceFuncPath", "filePaths")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKTYPE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    MAPREDUCEFUNCPATH_FIELD_NUMBER: _ClassVar[int]
    FILEPATHS_FIELD_NUMBER: _ClassVar[int]
    jobID: str
    taskType: TaskType
    taskID: int
    mapReduceFuncPath: FilePath
    filePaths: _containers.RepeatedCompositeFieldContainer[FilePath]
    def __init__(self, jobID: _Optional[str] = ..., taskType: _Optional[_Union[TaskType, str]] = ..., taskID: _Optional[int] = ..., mapReduceFuncPath: _Optional[_Union[FilePath, _Mapping]] = ..., filePaths: _Optional[_Iterable[_Union[FilePath, _Mapping]]] = ...) -> None: ...

class JustDoItResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
