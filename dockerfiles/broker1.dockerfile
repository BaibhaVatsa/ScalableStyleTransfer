FROM ubuntu:latest

RUN apt-get update
COPY kafka /kafka
CMD ["/kafka/bin/kafka-server-start.sh", "/kafka/config/server1.properties"]
