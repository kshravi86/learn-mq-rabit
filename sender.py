import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def send_message(message):
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(" [x] Sent %r" % message)

connection.close()
