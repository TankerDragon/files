FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install telethon

WORKDIR /usr/app/src

COPY client.py ./

CMD [ "python3", "./client.py" ]
