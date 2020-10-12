import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print('[x] Sent message: %r' % message)

connection.close()
