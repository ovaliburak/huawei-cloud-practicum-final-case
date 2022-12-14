import pika, json
credentials = pika.PlainCredentials('root', 'Root123@@')
params = pika.URLParameters(
    "amqps://vlnxnizd:YPMbDXGXw_1hlT7xE5vE962ApNaiY1J4@albatross.rmq.cloudamqp.com/vlnxnizd"
)

# connection = pika.BlockingConnection(params)
# parameters=pika.ConnectionParameters('192.168.1.94', 5672, '/', credentials)
# connection = pika.BlockingConnection(parameters)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, routing_key, body=None):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key=routing_key,
        body=json.dumps(body),
        properties=properties,
    )
