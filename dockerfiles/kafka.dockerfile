FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y default-jre
COPY kafka /kafka

