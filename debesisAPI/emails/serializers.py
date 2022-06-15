from rest_framework import serializers
from .models import Email, Template, Mailbox


class MailboxSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

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
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


    class Meta:
        model = Template
        fields = (
            "id",
            "subject",
            "text",
            "attachment",
            "date",
            "last_update",
        )


class EmailSerializer(serializers.ModelSerializer):
    # mailbox = MailboxSerializer(serializers.ModelSerializer)
    template = TemplateSerializer(serializers.ModelSerializer)
    sent_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

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
            "sent_date",
            "date",
        )
