# Import the pika library, which is used to interact with RabbitMQ
import pika

# Establish a connection to the RabbitMQ server on localhost
try:
    # Create a connection object using the BlockingConnection class
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
except pika.exceptions.AMQPConnectionError as e:
    # Handle connection errors
    print(f"Error connecting to RabbitMQ: {e}")
    exit(1)
# Create a channel, which is used to interact with RabbitMQ
channel = connection.channel()

# Declare a queue named 'hello' on the RabbitMQ server
try:
    # Use the queue_declare method to declare the queue
    channel.queue_declare(queue='hello')
except pika.exceptions.ChannelClosed as e:
    # Handle queue declaration errors
    print(f"Error declaring queue: {e}")
    exit(1)

# Define a function to send a message to the RabbitMQ queue
def send_message(message):
    """
    Send a message to the RabbitMQ queue.
    
    :param message: The message to send
    """
    # Use the basic_publish method to send the message to the queue
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    # Print a message indicating that the message has been sent
    print(" [x] Sent %r" % message)

# Close the connection to RabbitMQ
try:
    # Use the close method to close the connection
    connection.close()
except pika.exceptions.ConnectionClosed as e:
    # Handle connection closing errors
    print(f"Error closing connection: {e}")
if __name__ == "__main__":
    # Send a message to the queue
    send_message("Hello, RabbitMQ!")
