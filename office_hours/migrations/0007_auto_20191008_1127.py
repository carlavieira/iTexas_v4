# Generated by Django 2.2.5 on 2019-10-08 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0006_auto_20191008_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officehour',
            name='checkin_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Hora do check-in'),
        ),
        migrations.AlterField(
            model_name='officehour',
            name='checkout_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Hora do check-out'),
        ),
    ]