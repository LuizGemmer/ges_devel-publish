# Generated by Django 5.1.7 on 2025-03-27 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='sitacao',
            new_name='situacao',
        ),
    ]
