import pytest
from send import Mail

from pydantic_settings import BaseSettings, SettingsConfigDict
import pathlib

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=f"{pathlib.Path(__file__).parent.absolute()}/.env",
                                  env_file_encoding="utf-8", extra='ignore')

    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str

settings = Settings()


to_mail = "mymail@gmail.com" # Email to send
title = "Test" # Test title
body = "<h1>Тест H1</h1>\n\n<p>Test p</p>" # Test body

@pytest.mark.asyncio
async def test_mail_connect():
    email = Mail(settings.smtp_server, settings.smtp_port, settings.smtp_username, settings.smtp_password, True)

    email = Mail(settings.smtp_server, settings.smtp_port, "qwerty@exe.com", "123qwe")
    with pytest.raises(Exception):
        await email.smtp_async.connect()


@pytest.mark.asyncio
async def test_send_mail():
    email = Mail(settings.smtp_server, settings.smtp_port, settings.smtp_username, settings.smtp_password, True)

    res = await email.send(to_mail, title, body)
    assert res == True





