.PHONY: all service link-gen clean
# 定义.proto文件的路径
PROTO_DIR = protos

# 定义生成的Python文件的输出路径
GEN_DIR = gen
SERVICE_OUT_DIR = $(GEN_DIR)

# 定义.proto文件
SERVICE_PROTO = $(PROTO_DIR)/service.proto

# 定义protoc命令
PROTOC_CMD = python3 -m grpc_tools.protoc -I$(PROTO_DIR)

# 默认目标
service: $(SERVICE_PROTO) clean
	@mkdir -p $(SERVICE_OUT_DIR)
	@$(PROTOC_CMD) --python_out=$(SERVICE_OUT_DIR) --grpc_python_out=$(SERVICE_OUT_DIR) --pyi_out=$(SERVICE_OUT_DIR) $(SERVICE_PROTO)
	@sed -i '' 's/import \(.*\) as \(.*\)/from . import \1 as \2/g' $(SERVICE_OUT_DIR)/service_pb2_grpc.py

link-gen: service
	@ln -sfn $(CURDIR)/gen $(CURDIR)/master/gen
	@ln -sfn $(CURDIR)/gen $(CURDIR)/client/gen
	@ln -sfn $(CURDIR)/gen $(CURDIR)/worker/gen

all: link-gen

clean:
	@rm -rf $(GEN_DIR)/*
	@rm -rf $(CURDIR)/master/gen
	@rm -rf $(CURDIR)/client/gen
	@rm -rf $(CURDIR)/worker/gen
