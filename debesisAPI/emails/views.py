from django.shortcuts import render
from rest_framework import viewsets

from debesisAPI.emails.serializers import MailboxSerializer


class EmailsViewSet(viewsets.ModelViewSet):
    serializer_class = MailboxSerializer
    queryset = Mailbox.objects.all()
    pass
