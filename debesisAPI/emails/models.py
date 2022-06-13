from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


#Mailbox
class Mailbox(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    host = models.CharField()
    port = models.IntegerField(default='465')
    login = models.CharField()
    password = models.CharField()
    email_from = models.CharField()
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    sent = models.IntegerField()

    @property
    def count_emails(self):
        return self.sent


#Template
class Template(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    subject = models.CharField()
    text = models.TextField()
    attachment = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)


#Email
class Email(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    mailbox = models.ForeignKey(Mailbox, related_name='emails', on_delete=models.CASCADE)
    template = models.ForeignKey(Template, related_name='templates', on_delete=models.CASCADE)
    to = ArrayField(models.CharField())
    cc = ArrayField(models.CharField(null=True, blank=True))
    bcc = ArrayField(models.CharField(null=True, blank=True))
    reply_to = models.EmailField(default=None, null=True, blank=True)
    sent_date = models.DateTimeField(default=None)
    date = models.DateTimeField(auto_now_add=True)
