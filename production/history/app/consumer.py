import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "history.settings")
django.setup()

from core.models import History

params = pika.URLParameters(
    "amqps://vlnxnizd:YPMbDXGXw_1hlT7xE5vE962ApNaiY1J4@albatross.rmq.cloudamqp.com/vlnxnizd"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="history")


def callback(ch, method, properties, body):
    data = json.loads(body)
    if properties.content_type == "history_created":
        history=History.objects.create(
            product_id=data.get("product_id"),
            customer_id=data.get("customer_id"),
            employee_id=data.get("employee_id"),
            price=data.get("price"))
        history.save()


channel.basic_consume(queue="history", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()

