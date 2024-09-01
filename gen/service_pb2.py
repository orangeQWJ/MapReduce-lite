# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x06master\")\n\rServerAddress\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"F\n\x08\x46ilePath\x12,\n\rserverAddress\x18\x01 \x01(\x0b\x32\x15.master.ServerAddress\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x1c\n\tFileChunk\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"B\n\x15RegisterWorkerRequest\x12)\n\nserver_add\x18\x01 \x01(\x0b\x32\x15.master.ServerAddress\")\n\x16RegisterWorkerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"{\n\x11ReportTaskRequest\x12\r\n\x05jobID\x18\x01 \x01(\t\x12\"\n\x08taskType\x18\x02 \x01(\x0e\x32\x10.master.TaskType\x12\x0e\n\x06taskID\x18\x03 \x01(\x05\x12#\n\tfilePaths\x18\x04 \x03(\x0b\x32\x10.master.FilePath\"%\n\x12ReportTaskResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xb5\x01\n\x10UploadJobRequest\x12\x0e\n\x06mapNum\x18\x01 \x01(\x05\x12\x11\n\treduceNum\x18\x02 \x01(\x05\x12,\n\rserverAddress\x18\x03 \x01(\x0b\x32\x15.master.ServerAddress\x12+\n\x11mapReduceFuncPath\x18\x04 \x01(\x0b\x32\x10.master.FilePath\x12#\n\tfilePaths\x18\x05 \x03(\x0b\x32\x10.master.FilePath\"3\n\x11UploadJobResponse\x12\r\n\x05jobID\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"#\n\x0fReadFileRequest\x12\x10\n\x08\x66ilePath\x18\x01 \x01(\t\"M\n\x17ReportCompletionRequest\x12\r\n\x05jobID\x18\x01 \x01(\t\x12#\n\tfilePaths\x18\x02 \x03(\x0b\x32\x10.master.FilePath\"+\n\x18ReportCompletionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xa6\x01\n\x0fJustDoItRequest\x12\r\n\x05jobID\x18\x01 \x01(\t\x12\"\n\x08taskType\x18\x02 \x01(\x0e\x32\x10.master.TaskType\x12\x0e\n\x06taskID\x18\x03 \x01(\x05\x12+\n\x11mapReduceFuncPath\x18\x04 \x01(\x0b\x32\x10.master.FilePath\x12#\n\tfilePaths\x18\x05 \x03(\x0b\x32\x10.master.FilePath\"#\n\x10JustDoItResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08*\x1f\n\x08TaskType\x12\x07\n\x03MAP\x10\x00\x12\n\n\x06REDUCE\x10\x01\x32\xea\x01\n\x06Master\x12@\n\tUploadJob\x12\x18.master.UploadJobRequest\x1a\x19.master.UploadJobResponse\x12O\n\x0eRegisterWorker\x12\x1d.master.RegisterWorkerRequest\x1a\x1e.master.RegisterWorkerResponse\x12M\n\x14ReportTaskCompletion\x12\x19.master.ReportTaskRequest\x1a\x1a.master.ReportTaskResponse2\x99\x01\n\x06\x43lient\x12\x38\n\x08ReadFile\x12\x17.master.ReadFileRequest\x1a\x11.master.FileChunk0\x01\x12U\n\x10ReportCompletion\x12\x1f.master.ReportCompletionRequest\x1a .master.ReportCompletionResponse2\x81\x01\n\x06Worker\x12\x38\n\x08ReadFile\x12\x17.master.ReadFileRequest\x1a\x11.master.FileChunk0\x01\x12=\n\x08JustDoIt\x12\x17.master.JustDoItRequest\x1a\x18.master.JustDoItResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TASKTYPE']._serialized_start=1049
  _globals['_TASKTYPE']._serialized_end=1080
  _globals['_SERVERADDRESS']._serialized_start=25
  _globals['_SERVERADDRESS']._serialized_end=66
  _globals['_FILEPATH']._serialized_start=68
  _globals['_FILEPATH']._serialized_end=138
  _globals['_FILECHUNK']._serialized_start=140
  _globals['_FILECHUNK']._serialized_end=168
  _globals['_REGISTERWORKERREQUEST']._serialized_start=170
  _globals['_REGISTERWORKERREQUEST']._serialized_end=236
  _globals['_REGISTERWORKERRESPONSE']._serialized_start=238
  _globals['_REGISTERWORKERRESPONSE']._serialized_end=279
  _globals['_REPORTTASKREQUEST']._serialized_start=281
  _globals['_REPORTTASKREQUEST']._serialized_end=404
  _globals['_REPORTTASKRESPONSE']._serialized_start=406
  _globals['_REPORTTASKRESPONSE']._serialized_end=443
  _globals['_UPLOADJOBREQUEST']._serialized_start=446
  _globals['_UPLOADJOBREQUEST']._serialized_end=627
  _globals['_UPLOADJOBRESPONSE']._serialized_start=629
  _globals['_UPLOADJOBRESPONSE']._serialized_end=680
  _globals['_READFILEREQUEST']._serialized_start=682
  _globals['_READFILEREQUEST']._serialized_end=717
  _globals['_REPORTCOMPLETIONREQUEST']._serialized_start=719
  _globals['_REPORTCOMPLETIONREQUEST']._serialized_end=796
  _globals['_REPORTCOMPLETIONRESPONSE']._serialized_start=798
  _globals['_REPORTCOMPLETIONRESPONSE']._serialized_end=841
  _globals['_JUSTDOITREQUEST']._serialized_start=844
  _globals['_JUSTDOITREQUEST']._serialized_end=1010
  _globals['_JUSTDOITRESPONSE']._serialized_start=1012
  _globals['_JUSTDOITRESPONSE']._serialized_end=1047
  _globals['_MASTER']._serialized_start=1083
  _globals['_MASTER']._serialized_end=1317
  _globals['_CLIENT']._serialized_start=1320
  _globals['_CLIENT']._serialized_end=1473
  _globals['_WORKER']._serialized_start=1476
  _globals['_WORKER']._serialized_end=1605
# @@protoc_insertion_point(module_scope)