#!/usr/bin/env bash
python manage.py rqworker high &
python manage.py runserver 0.0.0.0:8000