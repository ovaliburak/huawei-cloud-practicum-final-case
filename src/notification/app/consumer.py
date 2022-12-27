import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notification.settings")
django.setup()

# from core.models import Customer, Employee

params = pika.URLParameters(
    "amqps://vlnxnizd:YPMbDXGXw_1hlT7xE5vE962ApNaiY1J4@albatross.rmq.cloudamqp.com/vlnxnizd"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="notification")


def callback(ch, method, properties, body):
    print(body)
    data = json.loads(body)
    print(data)
    print(body)

        



channel.basic_consume(queue="notification", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
