FROM python:3.10.8-slim-buster

RUN mkdir /app
RUN mkdir /app/api

RUN python3 -m venv /app/venv

COPY requirements.txt /app
COPY settings.ini /app
COPY /api /app/api

WORKDIR /app

RUN venv/bin/pip3 install -r /app/requirements.txt --no-cache-dir

CMD ["venv/bin/uvicorn", "api:app","--host", "0", "--port", "8000", "--proxy-headers"]
