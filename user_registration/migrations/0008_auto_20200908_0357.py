# Generated by Django 2.2.16 on 2020-09-08 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0007_auto_20200908_0328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verification',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='verification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 8, 3, 57, 41, 561393)),
        ),
    ]
