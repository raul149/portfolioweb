#!/bin/bash
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn portfolio.wsgi:application
