# FROM python:3.9
# ENV PYTHONUNBUFFERED 1
# WORKDIR /app
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt
# COPY . /app

# CMD python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000

FROM python:3.8.10-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh
    #chmod +x migrate.sh
#RUN sh /app/migrate.sh

CMD ["/app/entrypoint.sh"]
