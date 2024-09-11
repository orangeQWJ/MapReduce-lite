# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import service_pb2 as service__pb2
import service_pb2 as service__grpc

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
        + f' but the generated code in service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MasterStub(object):
    """定义 MasterService 服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadJob = channel.unary_unary(
                '/service.Master/UploadJob',
                request_serializer=service__pb2.UploadJobRequest.SerializeToString,
                response_deserializer=service__pb2.UploadJobResponse.FromString,
                _registered_method=True)
        self.RegisterWorker = channel.unary_unary(
                '/service.Master/RegisterWorker',
                request_serializer=service__pb2.RegisterWorkerRequest.SerializeToString,
                response_deserializer=service__pb2.RegisterWorkerResponse.FromString,
                _registered_method=True)
        self.ReportTaskCompletion = channel.unary_unary(
                '/service.Master/ReportTaskCompletion',
                request_serializer=service__pb2.ReportTaskRequest.SerializeToString,
                response_deserializer=service__pb2.ReportTaskResponse.FromString,
                _registered_method=True)


class MasterServicer(object):
    """定义 MasterService 服务
    """

    def UploadJob(self, request, context):
        """client -> master, 提交一个总的计算任务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterWorker(self, request, context):
        """worker -> master, worker向master注册
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportTaskCompletion(self, request, context):
        """worker -> master, 完成m/r Task后汇报
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadJob': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadJob,
                    request_deserializer=service__pb2.UploadJobRequest.FromString,
                    response_serializer=service__pb2.UploadJobResponse.SerializeToString,
            ),
            'RegisterWorker': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterWorker,
                    request_deserializer=service__pb2.RegisterWorkerRequest.FromString,
                    response_serializer=service__pb2.RegisterWorkerResponse.SerializeToString,
            ),
            'ReportTaskCompletion': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportTaskCompletion,
                    request_deserializer=service__pb2.ReportTaskRequest.FromString,
                    response_serializer=service__pb2.ReportTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.Master', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('service.Master', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Master(object):
    """定义 MasterService 服务
    """

    @staticmethod
    def UploadJob(request,
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
            '/service.Master/UploadJob',
            service__pb2.UploadJobRequest.SerializeToString,
            service__pb2.UploadJobResponse.FromString,
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
            '/service.Master/RegisterWorker',
            service__pb2.RegisterWorkerRequest.SerializeToString,
            service__pb2.RegisterWorkerResponse.FromString,
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
            '/service.Master/ReportTaskCompletion',
            service__pb2.ReportTaskRequest.SerializeToString,
            service__pb2.ReportTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ClientStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadFile = channel.unary_stream(
                '/service.Client/ReadFile',
                request_serializer=service__pb2.ReadFileRequest.SerializeToString,
                response_deserializer=service__pb2.FileChunk.FromString,
                _registered_method=True)
        self.ReportCompletion = channel.unary_unary(
                '/service.Client/ReportCompletion',
                request_serializer=service__pb2.ReportCompletionRequest.SerializeToString,
                response_deserializer=service__pb2.ReportCompletionResponse.FromString,
                _registered_method=True)


class ClientServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadFile(self, request, context):
        """worker -> client, worker从client获取文件，执行Map Task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportCompletion(self, request, context):
        """master -> client, master 向client汇报，整个任务都完成了
        并告知client去哪里拉取分散在worker节点中，Reduce任务的产物
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadFile,
                    request_deserializer=service__pb2.ReadFileRequest.FromString,
                    response_serializer=service__pb2.FileChunk.SerializeToString,
            ),
            'ReportCompletion': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportCompletion,
                    request_deserializer=service__pb2.ReportCompletionRequest.FromString,
                    response_serializer=service__pb2.ReportCompletionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.Client', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('service.Client', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Client(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/service.Client/ReadFile',
            service__pb2.ReadFileRequest.SerializeToString,
            service__pb2.FileChunk.FromString,
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
    def ReportCompletion(request,
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
            '/service.Client/ReportCompletion',
            service__pb2.ReportCompletionRequest.SerializeToString,
            service__pb2.ReportCompletionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class WorkerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadFile = channel.unary_stream(
                '/service.Worker/ReadFile',
                request_serializer=service__pb2.ReadFileRequest.SerializeToString,
                response_deserializer=service__pb2.FileChunk.FromString,
                _registered_method=True)
        self.JustDoIt = channel.unary_unary(
                '/service.Worker/JustDoIt',
                request_serializer=service__pb2.JustDoItRequest.SerializeToString,
                response_deserializer=service__pb2.JustDoItResponse.FromString,
                _registered_method=True)


class WorkerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadFile(self, request, context):
        """读取大文件服务，使用流式 RPC 传输数据
        worker->worker, client->worker
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JustDoIt(self, request, context):
        """master->worker, master 下发m/r task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadFile,
                    request_deserializer=service__pb2.ReadFileRequest.FromString,
                    response_serializer=service__pb2.FileChunk.SerializeToString,
            ),
            'JustDoIt': grpc.unary_unary_rpc_method_handler(
                    servicer.JustDoIt,
                    request_deserializer=service__pb2.JustDoItRequest.FromString,
                    response_serializer=service__pb2.JustDoItResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('service.Worker', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/service.Worker/ReadFile',
            service__pb2.ReadFileRequest.SerializeToString,
            service__pb2.FileChunk.FromString,
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
    def JustDoIt(request,
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
            '/service.Worker/JustDoIt',
            service__pb2.JustDoItRequest.SerializeToString,
            service__pb2.JustDoItResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
