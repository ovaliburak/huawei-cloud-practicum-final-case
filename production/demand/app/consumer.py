import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demand.settings")
django.setup()

from core.models import Customer, Employee, Demand

params = pika.URLParameters(
    "amqps://vlnxnizd:YPMbDXGXw_1hlT7xE5vE962ApNaiY1J4@albatross.rmq.cloudamqp.com/vlnxnizd"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="demand")


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
   
    if properties.content_type == "demand_created":
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
            customer = Customer.objects.get(customer_phone_number=data.get("customer_phone_number"))
        except Customer.DoesNotExist:
            customer = Customer.objects.create(
                id=data.get("customer_id"),
                customer_first_name=data.get("customer_first_name"),
                customer_last_name=data.get("customer_last_name"),
                customer_phone_number=data.get("customer_phone_number"),
            )
            customer.save()
        try:
            demand = Demand.objects.create(
                property_type=data.get("property_type"),
                sqft=data.get("sqft"),
                room_number=data.get("room_number"),
                year_built=data.get("year_built"),
                floor=data.get("floor"),
                total_floor=data.get("total_floor"),
                bathroom_number=data.get("bathroom_number"),
                price=data.get("price"),
                province=data.get("province"),
                district=data.get("district"),
                facade=data.get("facade"),
                employee=employee, 
                customer=customer
            )
            demand.save()
        except:
            pass
    # elif properties.content_type == "customer_updated":
    # product = Product.query.get(data["id"])
    # product.title = data["title"]
    # product.image = data["image"]
    # db.session.commit()
    # print("Product Updated")

    # elif properties.content_type == "customer_deleted":
    # Customer.objects.filter(phone_number=data.get("phone_number")).delete()


channel.basic_consume(queue="demand", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
