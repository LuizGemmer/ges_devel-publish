from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Tasks

# Create your views here.
class TasksIndex(LoginRequiredMixin, generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Tasks.objects.all()
    
class CreateTaskView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'tasks/create_update_task.html'
    model = Tasks
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')

    def form_valid(self, form):
        data = form.cleaned_data
        
        ## If the task is completed and the completion date is not set, set it to now
        if data['situacao'] == 'Concluída' and data['data_conclusao'] is None:
            form.instance.data_conclusao = timezone.now()

        ## If the task is not completed and the completion date is set, return an error to the user
        if data['situacao'] != 'Concluida' and data['data_conclusao'] is not None:
            form.add_error('data_conclusao', 'Data de conclusão só pode ser preenchida se a tarefa estiver concluída.')

        return super().form_valid(form)
