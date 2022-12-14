FROM python:3.8.10-slim

COPY . /app
WORKDIR /app


RUN pip install pip --upgrade && \
    pip install -r requirements.txt && \
    chmod +x entrypoint.sh \
    chmod +x migrate.sh

RUN sh /app/migrate.sh

CMD ["/app/entrypoint.sh"]
