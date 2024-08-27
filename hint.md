mapreduce_project/
│
├── proto/
│   ├── client.proto            # Client gRPC 服务的定义
│   ├── master.proto            # Master gRPC 服务的定义
│   ├── worker.proto            # Worker gRPC 服务的定义
│
├── gen/                        # 统一存放生成文件的目录
│   ├── client/                 # 存放 client.proto 生成的文件
│   │   ├── client_pb2.py       
│   │   ├── client_pb2_grpc.py  
│   ├── master/                 # 存放 master.proto 生成的文件
│   │   ├── master_pb2.py       
│   │   ├── master_pb2_grpc.py  
│   ├── worker/                 # 存放 worker.proto 生成的文件
│   │   ├── worker_pb2.py       
│   │   ├── worker_pb2_grpc.py  
│
├── client/
│   ├── client_service.py       # Client gRPC 服务端实现
│   ├── client_main.py          # Client 程序入口
│
├── master/
│   ├── master_service.py       # Master gRPC 服务端实现
│   ├── master_main.py          # Master 程序入口
│
├── worker/
│   ├── worker_service.py       # Worker gRPC 服务端实现
│   ├── worker_main.py          # Worker 程序入口
│
├── utils/
│   ├── utils.py                # 共享的实用工具函数
│
├── README.md                   # 项目说明文件
├── requirements.txt            # Python 依赖项
├── run_all.sh                  # 启动所有节点的脚本
└── Makefile                    # Makefile 文件，用于生成中间代码

