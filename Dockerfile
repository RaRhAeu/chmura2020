FROM python:3.8-buster

RUN sudo apt-get update && install default-libmysqlclient-dev build-essential -y
RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY ./service /

CMD ["/bin/bash", "./run.sh"]
