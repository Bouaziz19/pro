# Generated by Django 2.0.9 on 2020-03-14 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200314_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_res',
            name='star_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 28, 41, 619172)),
        ),
        migrations.AlterField(
            model_name='log_res',
            name='stop_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 28, 41, 619201)),
        ),
    ]
