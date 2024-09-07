import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def send_message(message):
    """
    Send a message to the RabbitMQ queue.
    
    :param message: The message to send
    """
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(" [x] Sent %r" % message)

try:
    connection.close()
finally:
    pass
