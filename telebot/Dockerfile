FROM python:3.8-slim-buster

WORKDIR /app

#COPY requirements.txt requirements.txt

RUN pip3 install telethon

COPY . .

EXPOSE 8000

CMD ["python3", "client.py"]

