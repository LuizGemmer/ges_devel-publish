from django.forms import ModelForm
from django import forms
from .models import Tasks

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['descricao', 'data_prevista']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_prevista': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class TaskUpdateForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['descricao', 'data_prevista', 'situacao', 'data_conclusao']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_prevista': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'situacao': forms.Select(attrs={'class': 'form-control'}),
            'data_conclusao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }