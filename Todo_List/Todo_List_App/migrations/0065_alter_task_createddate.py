# Generated by Django 4.2 on 2023-09-10 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0064_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 14, 57, 0, 588665, tzinfo=datetime.timezone.utc)),
        ),
    ]
