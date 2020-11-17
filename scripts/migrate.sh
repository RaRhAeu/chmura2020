#!/usr/bin/env bash
# Script for altering table when data model changes (or fresh db instance is connected)

docker exec -it rest-api python manage.py makemigrations
docker exec -it rest-api python manage.py migrate
