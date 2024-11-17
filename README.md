# API and Worker with RabbitMQ for send msg to email.

# Use

    smtp_server = "smtp.some.com"  # SMTP server address
    smtp_port = 465  # SMTP port
    smtp_username = "no-reply@exe.ru"  # SMTP email
    smtp_password = "password"  # SMTP passwd from email
    to_mail = "mymail@gmail.com" # Email to send
    title = "Test" # Test title
    body = "<h1>Тест H1</h1>\n\n<p>Test p</p>" # Test body
    
    async def main():
        email = Mail(smtp_server, smtp_port, smtp_username, smtp_password, ssl=True)
        await email.connect()
        res = await email.send(to_mail, title, body)
        
    


