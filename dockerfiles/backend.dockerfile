FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-requests
RUN apt-get install -y python3-kafka

COPY backendlul.py /backendlul.py
CMD ["python3", "/backendlul.py"]
