import pika
import os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)

try:
    connection = pika.BlockingConnection(params)
    print("Connected to RabbitMQ")
except pika.exceptions.AMQPError as e:
    print(f"Error connecting to RabbitMQ: {e}")
    exit(1)

channel = connection.channel()  # start a channel
channel.queue_declare(queue='test_queue')


def callback(ch, method, properties, body):
    print(' [x] Received ' + str(body))


channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
