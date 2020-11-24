FROM python:3.8-buster

RUN apt-get update -y

WORKDIR /app

COPY ./service /app

RUN pip install --upgrade pip && pip install -r ./requirements.txt
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]