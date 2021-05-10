FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-requests
RUN apt-get install -y python3-kafka

COPY backend.py /backend.py
CMD ["python3", "/backend.py"]
