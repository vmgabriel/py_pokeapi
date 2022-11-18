FROM python:3.10-alpine
LABEL Name=python-pokeapi

RUN apk update && apk upgrade && apk add git
COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY . /app/
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=:/app

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main:app"]