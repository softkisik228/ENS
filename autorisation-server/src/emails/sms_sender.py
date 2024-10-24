import smtplib
from email.message import EmailMessage

from celery import Celery

from config import SMTP_USER, SMTP_PASS


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')

def get_email_template(message: str, recipient: str):
    email = EmailMessage()
    email['Subject'] = 'ENS Sistem'
    email['From'] = SMTP_USER
    email['To'] = recipient
    email.set_content(message)
    return email

@celery.task
def send_email_notification(message: str, recipient: str):
    email = get_email_template(message, recipient)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
