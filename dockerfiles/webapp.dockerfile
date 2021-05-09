FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-requests
RUN apt-get install -y python3-flask

COPY form.py /form.py
RUN cd /
RUN mkdir templates
COPY templates/form.html /templates/form.html
COPY templates/data.html /templates/data.html
CMD ["python3", "/form.py"]
