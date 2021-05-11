FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y default-jre
COPY kafka /kafka
COPY config /config
CMD ["/kafka/bin/zookeeper-server-start.sh", "/config/zookeeper.properties"]

