# Generated by Django 2.2.5 on 2019-10-07 23:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0003_auto_20191007_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officehour',
            name='checkin_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Hora do check-in'),
        ),
        migrations.AlterField(
            model_name='officehour',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Dia'),
        ),
    ]
