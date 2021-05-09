FROM ubuntu:latest

RUN apt-get update
COPY kafka /kafka
CMD ["/kafka/bin/zookeeper-server-start.sh", "/kafka/config/zookeeper.properties"]

