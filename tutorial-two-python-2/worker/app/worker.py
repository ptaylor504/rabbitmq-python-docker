import pika
import time
import os
import sys

print("[*] Starting worker")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))

channel = connection.channel()

channel.queue_declare(
    queue='task_queue',
    durable=True
)


def callback(ch, method, properties, body):
    print("[*] Received message: %r" % body.decode())
    time.sleep(body.count(b'.'))
    print("[*] Done with %r" % body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue='task_queue',
    on_message_callback=callback
)

print("[*] Waiting for messages. Press CTRL+C to quit")

channel.start_consuming()
