FROM python:latest

RUN mkdir -p /home/app &&\
    mkdir -p /test-volume

COPY . /home/app

CMD ["python", "/home/app/main.py"]