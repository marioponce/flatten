FROM python:3.8.4-slim-buster

COPY . usr/scr/flatten
WORKDIR /usr/scr/flatten

RUN pip install -r requirements.txt