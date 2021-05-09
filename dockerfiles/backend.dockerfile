FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-kafka
RUN apt-get install -y python3-requests

COPY consumer.py /consumer.py
