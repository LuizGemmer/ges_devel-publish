from django.urls import path

from .views import index

urlpatterns = [
    path('tasks/', index.as_view(), name='tasks_index'),
]