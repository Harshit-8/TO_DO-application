# Generated by Django 4.2 on 2023-06-08 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0009_task_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 6, 16, 22, 21589, tzinfo=datetime.timezone.utc)),
        ),
    ]
