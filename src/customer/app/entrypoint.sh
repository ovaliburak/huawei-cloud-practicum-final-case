#!/bin/bash
APP_PORT=${PORT:-4000}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm customer.wsgi:application --bind "0.0.0.0:${APP_PORT}"
