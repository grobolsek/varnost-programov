FROM python:3.14-alpine
WORKDIR /app
ENV FLAG="flag{fake_flag}"

RUN pip install --no-cache-dir flask
COPY server.py /app
CMD ["python", "server.py"]
