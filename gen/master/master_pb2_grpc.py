# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import master_pb2 as master__pb2

GRPC_GENERATED_VERSION = '1.66.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in master_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MasterServiceStub(object):
    """定义 MasterService 服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadTask = channel.unary_unary(
                '/master.MasterService/UploadTask',
                request_serializer=master__pb2.UploadTaskRequest.SerializeToString,
                response_deserializer=master__pb2.UploadTaskResponse.FromString,
                _registered_method=True)
        self.RegisterWorker = channel.unary_unary(
                '/master.MasterService/RegisterWorker',
                request_serializer=master__pb2.RegisterWorkerRequest.SerializeToString,
                response_deserializer=master__pb2.RegisterWorkerResponse.FromString,
                _registered_method=True)
        self.ReportTaskCompletion = channel.unary_unary(
                '/master.MasterService/ReportTaskCompletion',
                request_serializer=master__pb2.ReportTaskRequest.SerializeToString,
                response_deserializer=master__pb2.ReportTaskResponse.FromString,
                _registered_method=True)


class MasterServiceServicer(object):
    """定义 MasterService 服务
    """

    def UploadTask(self, request, context):
        """上传任务服务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterWorker(self, request, context):
        """Worker 注册服务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportTaskCompletion(self, request, context):
        """Worker 汇报任务完成服务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadTask,
                    request_deserializer=master__pb2.UploadTaskRequest.FromString,
                    response_serializer=master__pb2.UploadTaskResponse.SerializeToString,
            ),
            'RegisterWorker': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterWorker,
                    request_deserializer=master__pb2.RegisterWorkerRequest.FromString,
                    response_serializer=master__pb2.RegisterWorkerResponse.SerializeToString,
            ),
            'ReportTaskCompletion': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportTaskCompletion,
                    request_deserializer=master__pb2.ReportTaskRequest.FromString,
                    response_serializer=master__pb2.ReportTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'master.MasterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('master.MasterService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MasterService(object):
    """定义 MasterService 服务
    """

    @staticmethod
    def UploadTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/master.MasterService/UploadTask',
            master__pb2.UploadTaskRequest.SerializeToString,
            master__pb2.UploadTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterWorker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/master.MasterService/RegisterWorker',
            master__pb2.RegisterWorkerRequest.SerializeToString,
            master__pb2.RegisterWorkerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReportTaskCompletion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/master.MasterService/ReportTaskCompletion',
            master__pb2.ReportTaskRequest.SerializeToString,
            master__pb2.ReportTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
