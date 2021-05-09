FROM ubuntu:latest

RUN apt-get update
COPY kafka /kafka

