from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import Mailbox, Email, Template
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
    # filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = ('date', 'sent_date')