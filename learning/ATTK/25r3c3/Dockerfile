FROM python:3.14-slim
WORKDIR /app

ENV FLAG=flag{fake_flag}

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential wget && \
    wget -O /bin/landrun https://github.com/Zouuup/landrun/releases/download/v0.1.14/landrun-linux-amd64 && \
    chmod +x /bin/landrun && \
    pip install --no-cache-dir Flask

COPY validator.py config.json /app/
COPY templates /app/templates
COPY static /app/static
COPY inputs /app/inputs

CMD ["python", "validator.py"]
