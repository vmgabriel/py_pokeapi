FROM python:3.10-slim-buster
LABEL Name=python-pokeapi

RUN apt-get update && apt-get -y upgrade && apt-get install -y git
COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY . /app/
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=:/app

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main:app"]