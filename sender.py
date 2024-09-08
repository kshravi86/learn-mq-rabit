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

def send_message(message):
    """
    Send a message to the RabbitMQ queue.
    
    :param message: The message to send
    """
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(" [x] Sent %r" % message)

try:
    connection.close()
except pika.exceptions.ConnectionClosed as e:
    print(f"Error closing connection: {e}")
