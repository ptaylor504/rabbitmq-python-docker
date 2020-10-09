import pika
import time
import os
import sys

print("[*] Starting worker")


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[*] Received message: %r" % body.decode())
    time.sleep(body.count(b'.'))
    print("[*] Done with %r" % body.decode())


channel.basic_consume(
    queue='hello',
    auto_ack=True,
    on_message_callback=callback
)

print("[*] Waiting for messages. Press CTRL+C to quit")

channel.start_consuming()
