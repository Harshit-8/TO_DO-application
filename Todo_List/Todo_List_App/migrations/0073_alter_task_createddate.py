# Generated by Django 4.2 on 2023-09-14 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0072_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 17, 37, 54, 479941, tzinfo=datetime.timezone.utc)),
        ),
    ]
