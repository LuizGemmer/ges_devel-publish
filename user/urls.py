from django.urls import path, include

from .views import UserRegisterView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', UserRegisterView.as_view(), name='register'),
]