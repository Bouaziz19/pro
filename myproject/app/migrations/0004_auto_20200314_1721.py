# Generated by Django 2.0.9 on 2020-03-14 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_log_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_res',
            name='star_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 21, 40, 950069)),
        ),
        migrations.AddField(
            model_name='log_res',
            name='stop_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 21, 40, 950100)),
        ),
    ]
