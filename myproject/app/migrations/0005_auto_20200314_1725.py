# Generated by Django 2.0.9 on 2020-03-14 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200314_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_res',
            name='star_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 25, 4, 314428)),
        ),
        migrations.AlterField(
            model_name='log_res',
            name='stop_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 25, 4, 314453)),
        ),
    ]
