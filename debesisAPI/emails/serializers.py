from rest_framework import serializers
from .models import Email, Template, Mailbox


class MailboxSerializer(serializers.ModelSerializer):
    sent_data = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    data = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    sent = ''

    class Meta:
        model = Mailbox
        fields = (
            "id",
            "host",
            "port",
            "login",
            "password",
            "email_from",
            "use_ssl",
            "is_active",
            "date",
            "last_update",
            "sent"
        )


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = (
            "id",
            "subject",
            "attachment",
            "date",
            "last_update",
        )


class EmailSerializer(serializers.ModelSerializer):
    mailbox = MailboxSerializer(serializers.ModelSerializer)
    template = TemplateSerializer(serializers.ModelSerializer)
    sent_data = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    data = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Email
        fields = (
            "id",
            "mailbox",
            "template",
            "to",
            "cc",
            "bcc",
            "reply_to",
            "sent_data",
            "data",
        )
