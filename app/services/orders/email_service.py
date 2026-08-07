from email.message import EmailMessage

import aiosmtplib

from app.core.config import SMTP_FROM, SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD


class EmailService:
    async def send(
            self,
            to: str,
            subject: str,
            body: str
    ) -> None:
        message = EmailMessage()
        message["From"] = SMTP_FROM
        message["To"] = to
        message["Subject"] = subject

        message.set_content(body)

        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USERNAME,
            password=SMTP_PASSWORD,
            start_tls=True,
        )
