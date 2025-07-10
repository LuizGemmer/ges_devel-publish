import uuid

from django.db import models

# Create your models here.
class Tasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=255)

    data_prevista = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    situacao = models.CharField(max_length=50, choices=[
        ('pendente', 'Pendente'),
        ('em andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ], default='pendente')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao
    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=255)

class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=255)