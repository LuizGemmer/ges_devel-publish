# Generated by Django 5.1.7 on 2025-07-09 23:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_sitacao_tasks_situacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
    ]
