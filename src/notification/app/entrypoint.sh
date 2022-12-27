#!/bin/bash
#APP_PORT=${PORT:-8002}
cd /app/
#exec python consumer.py &
python manage.py runserver 0.0.0.0:8006
#gunicorn --worker-tmp-dir /dev/shm customer.wsgi:application --bind "0.0.0.0:${APP_PORT}"
