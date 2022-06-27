from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
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
    parser_classes = [MultiPartParser]
    queryset = Template.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        if email.mailbox.is_active:
            return send_mail_task.delay(email_id)
        return print('Mailbox is inactive!')

    # filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = ('date', 'sent_date')
