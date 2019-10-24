# Generated by Django 2.2.6 on 2019-10-24 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_auto_20191023_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='participations',
        ),
        migrations.AddField(
            model_name='meeting',
            name='participations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='meetings.Participation', verbose_name='Participantes'),
        ),
    ]