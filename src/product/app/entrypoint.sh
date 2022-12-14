#!/bin/bash
APP_PORT=${PORT:-8003}
cd /app/
exec python consumer.py &
gunicorn --worker-tmp-dir /dev/shm product.wsgi:application --bind "0.0.0.0:${APP_PORT}"
