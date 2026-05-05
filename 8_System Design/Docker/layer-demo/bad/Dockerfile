FROM ubuntu:22.04

# Layer 1
RUN apt-get update

# Layer 2
RUN apt-get install -y curl

# Layer 3 — 試圖刪除 cache，但 Layer 1 的 byte 仍存在
RUN rm -rf /var/lib/apt/lists/*
