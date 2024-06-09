import smtplib
from email.mime.text import MIMEText
from time import sleep
from celery import Celery

from src.config import SMTP_USER, SMTP_PASSWORD

#   Celery
celery = Celery("tasks", broker="amqp://guest:guest@127.0.0.1:5672")


# Create an order - run asynchronous with celery
@celery.task
def create_order(name, quantity):
    complete_time_per_item = 5
    sleep(complete_time_per_item * quantity)
    return f"Hi {name}, Your order has completed! order_quantity: {quantity}"


@celery.task
def get_email_template_dashboard(username):
    msg = MIMEText(f"{username} syka", "plain")
    msg["Subject"] = "test yopta"
    msg["From"] = SMTP_USER
    msg["To"] = "hoochmoove@gmail.com"

    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.ehlo()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(
        SMTP_USER, "hoochmoove@gmail.com", msg.as_string()
    )  # Отправка письма
    server.quit()
    return "Письмо успешно отправлено!"
