from celery import shared_task
from django.core.mail import EmailMessage, get_connection


@shared_task
def send_mail_task(email_msg, email_conn):
    # connection = get_connection(**email_conn)
    email_msg = EmailMessage(**email_msg, connection=get_connection(**email_conn))
    email_msg.content_subtype = 'plain'
    return email_msg.send(fail_silently=False)
