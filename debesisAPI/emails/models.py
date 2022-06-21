from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


# Mailbox
class Mailbox(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default='465')
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_from = models.CharField(max_length=100)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('host',)

    def __str__(self):
        return self.host

    @property
    def sent(self):
        return self.emails.count()


# Template
class Template(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    subject = models.CharField(max_length=100)
    text = models.TextField()
    attachment = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('subject',)

    def __str__(self):
        return self.subject


# Email
class Email(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    mailbox = models.ForeignKey(Mailbox, related_name='emails', on_delete=models.CASCADE)
    template = models.ForeignKey(Template, related_name='templates', on_delete=models.CASCADE)
    to = ArrayField(models.CharField(max_length=100))
    cc = ArrayField(models.CharField(max_length=100, blank=True, null=True))
    bcc = ArrayField(models.CharField(max_length=100, blank=True, null=True))
    reply_to = models.EmailField(default=None, null=True, blank=True)
    sent_date = models.DateTimeField(default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date', 'sent_date')
