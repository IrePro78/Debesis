from rest_framework import serializers
from .models import Email, Template, Mailbox


class MailboxSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

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
    attachment = serializers.FileField()
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

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
    sent_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=None, read_only=True)
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    cc = serializers.CharField(required=False, default=None)
    bcc = serializers.CharField(required=False, default=None)

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
