import pika
from schemas import CreateMessage

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='msg', arguments={'x-max-priority': 2})

async def add_new_msg_task(create_message: CreateMessage):
    if create_message.type == 'admin':
        channel.basic_publish(exchange='', routing_key='msg', body=create_message.json(), properties=pika.BasicProperties(priority=2))
    elif create_message.type == 'info':
        channel.basic_publish(exchange='', routing_key='msg', body=create_message.json(), properties=pika.BasicProperties(priority=1))
    else:
        channel.basic_publish(exchange='', routing_key='msg', body=create_message.json(), properties=pika.BasicProperties(priority=0))

    print("Add new msg")

async def close_rabbitmq():
    connection.close()
