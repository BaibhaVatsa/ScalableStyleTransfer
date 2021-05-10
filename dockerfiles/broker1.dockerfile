FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y default-jre
COPY kafka /kafka
CMD ["/kafka/bin/kafka-server-start.sh", "/kafka/config/server1.properties"]
