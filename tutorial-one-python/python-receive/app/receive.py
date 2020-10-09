import pika
import os
import sys

print("[*] Starting receiver")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print("[*] Received message: %r" % body)

    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )

    print("[*] Waiting for messages. Press CTRL+C to quit")

    channel.start_consuming()



if __name__ == '__main__':
    main()
    #try:
    #    main()
    #except:
    #    print('Error')

    #except KeyboardInterrupt:
    #    print('Interrupted')
        #try:
        #    sys.exit(0)
        #except SystemExit:
        #    os._exit(0)
