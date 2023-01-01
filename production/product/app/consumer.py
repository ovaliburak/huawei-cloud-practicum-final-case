import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product.settings")
django.setup()

from core.models import Product, Employee, Advert

params = pika.URLParameters(
    "amqps://vlnxnizd:YPMbDXGXw_1hlT7xE5vE962ApNaiY1J4@albatross.rmq.cloudamqp.com/vlnxnizd"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="product")


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(properties.content_type)
    if properties.content_type == "product_created":
        print(properties.content_type)
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
        product=Product.objects.create(
            property_type=data.get("property_type"),
            sqft=data.get("sqft"),
            room_number=data.get("room_number"),
            year_built=data.get("year_built"),
            floor=data.get("floor"),
            total_floor=data.get("total_floor"),
            bathroom_number=data.get("bathroom_number"),
            price=data.get("price"),
            province=data.get('province'),
            district=data.get('district'),
            facade=data.get("facade")
        )
        print(product)
    elif properties.content_type == "advert_created":
        print(data)
        try:
            employee = Employee.objects.get(id=data.get("employee_id"))
        except Employee.DoesNotExist:
            employee = Employee.objects.create(
                id=data.get("employee_id"),
                employee_first_name=data.get("employee_first_name"),
                employee_last_name=data.get("employee_last_name"),
                employee_phone_number=data.get("employee_phone_number"),
            )
            print(employee)
            employee.save()
        try:
            product = Product.objects.get(id=data.get("product_id"))
        except Product.DoesNotExist:
            product=None
        try:
            advert=Advert.objects.create(
                ad_type=data.get("ad_type"),
                product=product,
                advert_price=data.get("advert_price"),
                employee=employee
            )
            advert.save()
            product.sales=True
            print(product)
            product.save()
        except:
            pass
            
    elif properties.content_type == "product_sold":
        try:
            product = Product.objects.get(id=data.get("product_id"))
            product.sold = True
            product.sales = False
            product.save()
            try:
                advert = Advert.objects.filter(product=product).delete()
            except:
                pass
        except:
            pass



channel.basic_consume(queue="product", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
