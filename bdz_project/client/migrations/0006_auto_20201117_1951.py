# Generated by Django 2.2.12 on 2020-11-17 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20201117_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 19, 51, 40, 347821), verbose_name='created date'),
        ),
    ]
