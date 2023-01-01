#!/bin/bash
# APP_PORT=${PORT:-8001}
cd /app/
# gunicorn --worker-tmp-dir /dev/shm employee.wsgi:application --bind "0.0.0.0:${APP_PORT}"
python manage.py runserver 0.0.0.0:8001