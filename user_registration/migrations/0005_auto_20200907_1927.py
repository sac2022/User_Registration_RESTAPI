# Generated by Django 2.2.16 on 2020-09-07 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0004_auto_20200907_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 7, 19, 27, 21, 859668)),
        ),
    ]
