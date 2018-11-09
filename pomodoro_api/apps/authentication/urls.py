from django.urls import re_path

from .views import RegistrationAPIView

app_name = 'authentication'
urlpatterns = [
    re_path(r'^users/?$', RegistrationAPIView.as_view()),
]
