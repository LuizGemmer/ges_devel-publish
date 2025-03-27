from django.shortcuts import render
from django.views import generic

from .models import Tasks

# Create your views here.
class index(generic.ListView):
    template_name = 'tasks/base.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Tasks.objects.all()