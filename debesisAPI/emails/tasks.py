from celery import shared_task
from django.core.mail import EmailMessage, get_connection

from .models import Email


@shared_task
def send_mail_task(email_id):
    email = Email.objects.get(id=email_id)

    connection = get_connection(
        host=email.mailbox.host,
        port=email.mailbox.port,
        username=email.mailbox.login,
        password=email.mailbox.password,
        use_tls=email.mailbox.use_ssl
    )

    email_msg = {
        'subject': email.template.subject,
        'body': email.template.text,
        'from_email': email.mailbox.email_from,
        'to': email.to,
        'bcc': email.bcc,
        'connection': connection,
        'attachments': email.template.attachment,
        'headers': None,
        'cc': email.cc,
        'reply_to': email.reply_to,
    }

    message = EmailMessage(*tuple(email_msg.values()))
    message.attach_file('./attachments/test.pdf')
    message.send(fail_silently=False)
