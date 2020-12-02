import time, pika, os


"""

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

"""

rabbit_host = os.environ.get('RABBIT_HOST')
rabbit_port = os.environ.get('RABBIT_PORT')
rabbit_vhost = os.environ.get('RABBIT_VHOST')
rabbit_user = os.environ.get('RABBIT_USER')
rabbit_password = os.environ.get('RABBIT_PASSWORD')


cred = pika.PlainCredentials(rabbit_user, rabbit_password)
params = pika.ConnectionParameters(
    host= rabbit_host,
    port= rabbit_port,
    virtual_host= rabbit_vhost,
    credentials=cred
)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='test', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Message Received ")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test', on_message_callback=callback)

channel.start_consuming()