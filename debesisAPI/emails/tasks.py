from celery import shared_task
from django.core.mail import EmailMessage, get_connection


@shared_task
def send_mail_task(email_msg, email_conn):

    print(email_conn)



    connection = get_connection(
        host=email_conn['host'],
        port=email_conn['port'],
        username=email_conn['username'],
        password=email_conn['password'],
        tls=email_conn['tls'],
    )

    connection.open()

    email_msg = EmailMessage(*tuple(email_msg.values()))

    connection.send_messages([email_msg])
    connection.close()

    return True
