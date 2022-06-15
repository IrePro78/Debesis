from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmailsViewSet, MailboxViewSet, TemplateViewSet

router = DefaultRouter()
router.register('mailbox', MailboxViewSet, basename='mailbox')
router.register('template', TemplateViewSet, basename='template')
router.register('email', EmailsViewSet, basename='email')

urlpatterns = router.urls




# urlpatterns = [
#     path('', include(router.urls)),
#     path('mailbox/', include(router.urls)),
#     path('mailbox/:id/', include(router.urls)),
#     path('template/', include(router.urls)),
#     path('template/:id/', include(router.urls)),
#     path('template/:id/', include(router.urls)),
#
# ]

