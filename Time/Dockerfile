FROM ubuntu:26.04
WORKDIR /app

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get install -y socat coreutils && \
    rm -rf /var/lib/apt/lists/*

COPY flag.txt /app
COPY server /app
COPY entrypoint.sh /app

CMD ["/app/entrypoint.sh"]
