FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
