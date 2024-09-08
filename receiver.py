import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
except pika.exceptions.AMQPConnectionError as e:
    print(f"Error connecting to RabbitMQ: {e}")
    exit(1)
channel = connection.channel()

try:
    channel.queue_declare(queue='hello')
except pika.exceptions.ChannelClosed as e:
    print(f"Error declaring queue: {e}")
    exit(1)

def callback(ch, method, properties, body):
    """
    Callback function to process incoming messages.
    
    :param ch: The channel
    :param method: The method
    :param properties: The properties
    :param body: The message body
    """
    print(" [x] Received %r" % body)

try:
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
except pika.exceptions.ChannelClosed as e:
    print(f"Error consuming from queue: {e}")
    exit(1)

print(' [*] Waiting for messages. To exit press CTRL+C')
try:
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
except KeyboardInterrupt:
    print(' [*] Exiting')
finally:
    connection.close()
