# Import the pika library, which is used to interact with RabbitMQ
import pika

# Establish a connection to the RabbitMQ server on localhost
try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
except pika.exceptions.AMQPConnectionError as e:
    # Handle connection errors
    print(f"Error connecting to RabbitMQ: {e}")
    exit(1)
# Create a channel, which is used to interact with RabbitMQ
channel = connection.channel()

# Declare a queue named 'hello' on the RabbitMQ server
try:
    channel.queue_declare(queue='hello')
except pika.exceptions.ChannelClosed as e:
    # Handle queue declaration errors
    print(f"Error declaring queue: {e}")
    exit(1)

# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    """
    Callback function to process incoming messages.
    
    :param ch: The channel
    :param method: The method
    :param properties: The properties
    :param body: The message body
    """
    # Print a message indicating that a message has been received
    print(" [x] Received %r" % body)

# Set up a consumer to receive messages from the 'hello' queue
try:
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
except pika.exceptions.ChannelClosed as e:
    # Handle consumer setup errors
    print(f"Error consuming from queue: {e}")
    exit(1)

# Print a message indicating that the consumer is waiting for messages
print(' [*] Waiting for messages. To exit press CTRL+C')
try:
    # Start consuming messages from the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
except KeyboardInterrupt:
    # Handle keyboard interrupt (CTRL+C)
    print(' [*] Exiting')
finally:
    # Close the connection to RabbitMQ
    connection.close()
