import asyncio

from send.rabbitmq import send_msg


def main():
    while True:
        asyncio.run(send_msg())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print("Stop worker!")
