from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmailsViewSet

router = DefaultRouter()
router.register('emails', EmailsViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

