import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "customer.settings")
django.setup()

from core.models import Customer, Employee

params = pika.URLParameters(
    "amqps://vlnxnizd:YPMbDXGXw_1hlT7xE5vE962ApNaiY1J4@albatross.rmq.cloudamqp.com/vlnxnizd"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="customer")


def callback(ch, method, properties, body):
    data = json.loads(body)
    if properties.content_type == "customer_created":
        try:
            employee = Employee.objects.get(id=data.get("employee_id"))
        except Employee.DoesNotExist:
            employee = Employee.objects.create(
                id=data.get("employee_id"),
                employee_first_name=data.get("employee_first_name"),
                employee_last_name=data.get("employee_last_name"),
                employee_phone_number=data.get("employee_phone_number"),
            )
            employee.save()
        try:
            customer = Customer.objects.get(phone_number=data.get("phone_number"))
        except Customer.DoesNotExist:
            customer = Customer.objects.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                phone_number=data.get("phone_number"),
                employee=employee,
            )
            customer.save()
    # elif properties.content_type == "customer_updated":
        # product = Product.query.get(data["id"])
        # product.title = data["title"]
        # product.image = data["image"]
        # db.session.commit()
        # print("Product Updated")

    elif properties.content_type == "customer_deleted":
        Customer.objects.filter(phone_number=data.get("phone_number")).delete()


channel.basic_consume(queue="customer", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
