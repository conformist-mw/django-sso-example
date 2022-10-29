 FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1

RUN apt update && apt -y install libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY . /code/
WORKDIR /code
