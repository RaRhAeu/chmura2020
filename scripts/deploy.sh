#!/usr/bin/env bash

docker login -u rarhaeu -p "$DOCKER_PWD"

docker build --tag rarhaeu/chmura2020:latest .

docker push rarhaeu/chmura2020:latest
