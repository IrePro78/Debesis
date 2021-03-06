from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Mailbox, Email, Template
from datetime import datetime
from .serializers import MailboxSerializer, EmailSerializer, TemplateSerializer
from .tasks import send_mail_task


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

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        email = self.get_object()
        email.sent_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email.save()

        if email.mailbox.is_active:
            send_mail_task.delay(email.id)
            return Response(status=status.HTTP_200_OK)
        return Response('Mailbox is inactive', status=status.HTTP_401_UNAUTHORIZED)
