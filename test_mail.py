import pytest
from send import Mail

smtp_server = "smtp.some.com"  # SMTP server address
smtp_port = 465  # SMTP port
smtp_username = "no-reply@exe.ru"  # SMTP email
smtp_password = "password"  # SMTP passwd from email
to_mail = "mymail@gmail.com" # Email to send
title = "Test" # Test title
body = "<h1>Тест H1</h1>\n\n<p>Test p</p>" # Test body

@pytest.mark.asyncio
async def test_mail_connect():
    email = Mail(smtp_server, smtp_port, smtp_username, smtp_password, True)
    res = await email.connect()
    assert res == True
    res = await email.disconnect()
    assert res == True

    email = Mail(smtp_server, smtp_port, "qwerty@exe.com", "123qwe")
    with pytest.raises(Exception):
        await email.connect()


@pytest.mark.asyncio
async def test_send_mail():
    email = Mail(smtp_server, smtp_port, smtp_username, smtp_password, True)
    res = await email.connect()
    assert res == True

    res = await email.send(to_mail, title, body)
    assert res == True





