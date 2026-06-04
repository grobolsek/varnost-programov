FROM ubuntu:26.04
WORKDIR /app

ENV FLAG=flag{fake_flag}

RUN apt-get update && \
    apt-get install -y socat

COPY ./main /app/main
CMD ["socat", "-t", "30", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/app/main"]
