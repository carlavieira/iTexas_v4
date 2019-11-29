# Generated by Django 2.2.5 on 2019-10-04 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20190929_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_working',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='department',
            field=models.CharField(blank=True, choices=[('1', 'LCP'), ('2', 'PM'), ('3', 'F&L'), ('4', 'B2C'), ('5', 'B2B'), ('6', 'OGE'), ('7', 'OGT'), ('8', 'OGV'), ('9', 'IGE'), ('10', 'IGT')], max_length=2, null=True, verbose_name='Área'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Líder'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='post',
            field=models.CharField(blank=True, choices=[('LCP', 'LCP'), ('LCVP', 'LCVP'), ('3', 'TLB'), ('4', 'Membro')], max_length=2, null=True, verbose_name='Cargo'),
        ),
    ]
