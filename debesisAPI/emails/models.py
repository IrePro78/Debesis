from django.db import models
import uuid


class Mailbox(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    host = models.CharField(blank=True)
    port = models.IntegerField(default='465', blank=True)
    login = models.CharField(blank=True)
    password = models.CharField(blank=True)
    email_from = models.CharField(default=True, blank=True)
    use_ssl = models.BooleanField(default=True, blank=True)
    is_active = models.BooleanField()
    date = models.DateTimeField
    last_update = models.DateTimeField
    sent = models.IntegerField()

    @property
    def count_emails(self):
        return self.sent


class Mail(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    mailbox = models.ForeignKey(Mailbox, related_name='emails', on_delete=models.CASCADE
    template = models.ForeignKey(Template, blank=True)
    to = models.EmailField
    cc =
    bcc =
    reply_to =
    sent_date =
    date =
