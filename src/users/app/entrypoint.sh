#!/bin/bash
APP_PORT=${PORT:-6000}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm app.wsgi:application --bind "0.0.0.0:${APP_PORT}"