from celery import shared_task
from django.core.mail import EmailMessage, get_connection


@shared_task
def send_mail_task(email_msg, email_conn):

    connection = get_connection(
        # host=email_conn['host'],
        # port=email_conn['port'],
        # login=email_conn['login'],
        # password=email_conn['password'],
        # tls=email_conn['tls']
        host='smtp.gmail.com',
        port='587',
        login='flaskdjangopython@gmail.com',
        password='iyshvwucxvtkrvmh',
        tls='True'
    )
    print(connection)
    email_msg = EmailMessage(*tuple(email_msg.values()), connection)
    email_msg.content_subtype = 'plain'
    return email_msg.send(fail_silently=False)
