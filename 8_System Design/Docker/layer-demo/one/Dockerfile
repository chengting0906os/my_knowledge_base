FROM ubuntu:22.04
RUN for i in $(seq 1 50); do dd if=/dev/zero of=/tmp/dummy bs=1M count=10 2>/dev/null && rm /tmp/dummy; done
