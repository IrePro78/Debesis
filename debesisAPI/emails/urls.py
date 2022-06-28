from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmailsViewSet, MailboxViewSet, TemplateViewSet

router = DefaultRouter()
router.register('mailbox', MailboxViewSet, basename='mailbox')
router.register('template', TemplateViewSet, basename='template')
router.register('email', EmailsViewSet, basename='email')

urlpatterns = router.urls
