#!/bin/bash

echo "waiting for database..."
sleep 20

echo "Running migrations"
python manage.py makemigrations
python manage.py migrate

echo "Starting app"
python manage.py runserver 0.0.0.0:8000