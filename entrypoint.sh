#!/bin/bash
python3 manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000