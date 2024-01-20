import pika
import os
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channgel
channel.exchange_declare('test_exchange')  # declare exchange
channel.queue_declare(queue='test_queue')  # declare queue
# create binding between queue and exchange
channel.queue_bind('test_queue', 'test_exchange', 'tests')
channel.basic_publish(
    body='hello RabbitMQ!',
    exchange='test_exchange',
    routing_key='tests'
)
print('message sent.')
channel.close()
connection.close()
