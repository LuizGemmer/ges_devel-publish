from django.urls import path

from .views import TasksIndex, CreateTaskView

urlpatterns = [
    path('', TasksIndex.as_view(), name='tasks_index'),
    path('create/', CreateTaskView.as_view(), name='tasks_create'),
]