# 定义.proto文件的路径
PROTO_DIR = protos

# 定义生成的Python文件的输出路径
GEN_DIR = gen
CLIENT_OUT_DIR = $(GEN_DIR)/client
MASTER_OUT_DIR = $(GEN_DIR)/master
WORKER_OUT_DIR = $(GEN_DIR)/worker

# 定义.proto文件
CLIENT_PROTO = $(PROTO_DIR)/client.proto
MASTER_PROTO = $(PROTO_DIR)/master.proto
WORKER_PROTO = $(PROTO_DIR)/worker.proto

# 定义protoc命令
PROTOC_CMD = python3 -m grpc_tools.protoc -I$(PROTO_DIR)

# 默认目标
all: client master worker

# 生成client的中间代码
client: $(CLIENT_PROTO)
	mkdir -p $(CLIENT_OUT_DIR)
	$(PROTOC_CMD) --python_out=$(CLIENT_OUT_DIR) --grpc_python_out=$(CLIENT_OUT_DIR) --pyi_out=$(CLIENT_OUT_DIR) $(CLIENT_PROTO)

# 生成master的中间代码
master: $(MASTER_PROTO)
	mkdir -p $(MASTER_OUT_DIR)
	$(PROTOC_CMD) --python_out=$(MASTER_OUT_DIR) --grpc_python_out=$(MASTER_OUT_DIR) --pyi_out=$(MASTER_OUT_DIR) $(MASTER_PROTO)

# 生成worker的中间代码
worker: $(WORKER_PROTO)
	mkdir -p $(WORKER_OUT_DIR)
	$(PROTOC_CMD) --python_out=$(WORKER_OUT_DIR) --grpc_python_out=$(WORKER_OUT_DIR) --pyi_out=$(WORKER_OUT_DIR) $(WORKER_PROTO)

# 清理生成的文件
clean:
	rm -rf $(GEN_DIR)
