# Generated by Django 4.2 on 2023-06-18 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0053_alter_profile_profile_picture_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 18, 15, 28, 38, 956567, tzinfo=datetime.timezone.utc)),
        ),
    ]