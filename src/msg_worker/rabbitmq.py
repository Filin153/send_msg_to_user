import pika
from send import Mail
import asyncio
from config import settings
import json

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




async def close_rabbitmq():
    connection.close()