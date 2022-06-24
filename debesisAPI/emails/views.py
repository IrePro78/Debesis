from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Mailbox, Email, Template
from .tasks import send_mail_task
from .serializers import MailboxSerializer, EmailSerializer, TemplateSerializer


class MailboxViewSet(viewsets.ModelViewSet):
    serializer_class = MailboxSerializer
    queryset = Mailbox.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class TemplateViewSet(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class EmailFilter(filters.FilterSet):
    class Meta:
        model = Email
        fields = ['date', 'sent_date']


class EmailsViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.send_message(serializer.data['id'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_message(self, email_id):
        email = self.queryset.get(id=email_id)

        email_msg = {
            'subject': email.template.subject,
            'body': email.template.text,
            'from_email': email.mailbox.email_from,
            'to': email.to,
            'cc': email.cc,
            'bcc': email.bcc,
            'reply_to': email.reply_to,
            # 'attachments': email.template.attachment,
        }
        email_conn = {
            'host': email.mailbox.host,
            'port': email.mailbox.port,
            'username': email.mailbox.login,
            'password': email.mailbox.password,
            'tls': email.mailbox.use_ssl,
        }
        print(email_conn)

        return send_mail_task.delay(email_msg, email_conn)

    # filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = ('date', 'sent_date')
