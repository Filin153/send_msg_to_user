import asyncio

from send.mail import Mail


def main():
    mail = Mail()
    asyncio.run(mail._worker())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print("Stop worker!")
