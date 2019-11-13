

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('RG', 'Reunião Geral'), ('AS', 'Assembléia')], max_length=3, null=True, verbose_name='Tipo do Evento')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Dia')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Hora')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Líder')),
            ],
        ),
    ]
