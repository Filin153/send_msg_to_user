import logging
import smtplib


class SMTPAsync:
    def __init__(self, smtp_server: str, smtp_port: int,
                 smtp_username: str, smtp_password: str,
                 ssl: bool = False, tls: bool = False, timeout: int = 10):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.tls = tls
        self.ssl = ssl
        self.timeout = timeout

        self._server = None

    async def connect(self) -> bool:
        """
        Make connect to SMTP server with login
        :return:
        """
        if self.ssl:
            self._server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, timeout=self.timeout)
            logging.info("SMTP connection established, with SMTP_SSL")
        else:
            self._server = smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=self.timeout)
            logging.info("SMTP connection established")
            if self.tls:
                self._server.starttls()
                logging.info("TLS connection established")

        self._server.login(self.smtp_username, self.smtp_password)
        logging.info(f"Successful login as {self.smtp_username}")

        return True

    async def disconnect(self) -> bool:
        """
        Disconnect from SMTP server
        :return:
        """
        self._server.quit()
        logging.info("SMTP connection disconnected")
        return True

    @staticmethod
    def __check_correct_ssl_tls(ssl: bool, tls: bool) -> bool:
        """
        If ssl using with tls raise ValueError
        If ssl using without tls return True
        If tls using without ssl return True
        :param ssl:
        :param tls:
        :return:
        """
        if tls and ssl:
            raise ValueError("TLS and SSL are mutually exclusive")

        return True


class SMTPSync:
    def __init__(self, smtp_server: str, smtp_port: int,
                 smtp_username: str, smtp_password: str,
                 ssl: bool = False, tls: bool = False, timeout: int = 10):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.tls = tls
        self.ssl = ssl
        self.timeout = timeout

        self._server = None

    def connect(self) -> bool:
        """
        Make connect to SMTP server with login
        :return:
        """
        if self.ssl:
            self._server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, timeout=self.timeout)
            logging.info("SMTP connection established, with SMTP_SSL")
        else:
            self._server = smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=self.timeout)
            logging.info("SMTP connection established")
            if self.tls:
                self._server.starttls()
                logging.info("TLS connection established")

        self._server.login(self.smtp_username, self.smtp_password)
        logging.info(f"Successful login as {self.smtp_username}")

        return True

    def disconnect(self) -> bool:
        """
        Disconnect from SMTP server
        :return:
        """
        self._server.quit()
        logging.info("SMTP connection disconnected")
        return True

    @staticmethod
    def __check_correct_ssl_tls(ssl: bool, tls: bool) -> bool:
        """
        If ssl using with tls raise ValueError
        If ssl using without tls return True
        If tls using without ssl return True
        :param ssl:
        :param tls:
        :return:
        """
        if tls and ssl:
            raise ValueError("TLS and SSL are mutually exclusive")

        return True


class SMTP:
    def __init__(self, smtp_server: str, smtp_port: int,
                 smtp_username: str, smtp_password: str,
                 ssl: bool = False, tls: bool = False, timeout: int = 10):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.tls = tls
        self.ssl = ssl
        self.timeout = timeout

        self.smtp_sync = SMTPSync(smtp_server, smtp_port,
                                  smtp_username, smtp_password,
                                  ssl=ssl, tls=tls, timeout=timeout)

        self.smtp_async = SMTPAsync(smtp_server, smtp_port,
                                    smtp_username, smtp_password,
                                    ssl=ssl, tls=tls, timeout=timeout)

        self._server = None
