import pika
from send import Mail
from config import settings
import json
from .schemas import CreateMessage, TypeEnum


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='msg', arguments={'x-max-priority': 2})

email = Mail(settings.smtp_server, settings.smtp_port, settings.smtp_username, settings.smtp_password, True)

async def send_msg():
    def callback(ch, method, properties, body):
        body = json.loads(body)
        email.send_sync(body['send_to'], body['title'], body['message'])

    channel.basic_consume(queue='msg', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

async def add_new_msg_task(create_message: CreateMessage):
    if create_message.type == TypeEnum.admin:
        channel.basic_publish(exchange='', routing_key='msg', body=create_message.json(), properties=pika.BasicProperties(priority=2))
    elif create_message.type == TypeEnum.info:
        channel.basic_publish(exchange='', routing_key='msg', body=create_message.json(), properties=pika.BasicProperties(priority=1))
    else:
        channel.basic_publish(exchange='', routing_key='msg', body=create_message.json(), properties=pika.BasicProperties(priority=0))

    print("Add new msg")




async def close_rabbitmq():
    connection.close()