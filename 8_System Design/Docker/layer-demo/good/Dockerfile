FROM ubuntu:22.04

# 只有 1 個 layer，cache 在同一層清除，不寫入任何持久 layer
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*
