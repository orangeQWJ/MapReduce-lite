# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client.proto
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
    'client.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63lient.proto\x12\x06\x63lient\"2\n\x08\x46ilePath\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\"\x1c\n\tFileChunk\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"6\n\x0fReadFileRequest\x12#\n\tfile_path\x18\x01 \x01(\x0b\x32\x10.client.FilePath\"O\n\x17ReportCompletionRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12$\n\nfile_paths\x18\x02 \x03(\x0b\x32\x10.client.FilePath\"+\n\x18ReportCompletionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x9f\x01\n\x0c\x43lientSrvice\x12\x38\n\x08ReadFile\x12\x17.client.ReadFileRequest\x1a\x11.client.FileChunk0\x01\x12U\n\x10ReportCompletion\x12\x1f.client.ReportCompletionRequest\x1a .client.ReportCompletionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILEPATH']._serialized_start=24
  _globals['_FILEPATH']._serialized_end=74
  _globals['_FILECHUNK']._serialized_start=76
  _globals['_FILECHUNK']._serialized_end=104
  _globals['_READFILEREQUEST']._serialized_start=106
  _globals['_READFILEREQUEST']._serialized_end=160
  _globals['_REPORTCOMPLETIONREQUEST']._serialized_start=162
  _globals['_REPORTCOMPLETIONREQUEST']._serialized_end=241
  _globals['_REPORTCOMPLETIONRESPONSE']._serialized_start=243
  _globals['_REPORTCOMPLETIONRESPONSE']._serialized_end=286
  _globals['_CLIENTSRVICE']._serialized_start=289
  _globals['_CLIENTSRVICE']._serialized_end=448
# @@protoc_insertion_point(module_scope)
