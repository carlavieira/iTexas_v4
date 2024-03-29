# Generated by Django 2.2.5 on 2019-09-29 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('podio_code', models.BigIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=20, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=20, verbose_name='Sobrenome')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('post', models.CharField(blank=True, choices=[('LCP', 'LCP'), ('LCVP', 'LCVP'), ('TLB', 'TLB'), ('Membro', 'Membro')], max_length=1, null=True)),
                ('department', models.CharField(blank=True, choices=[('LCP', 'LCP'), ('PM', 'PM'), ('F&L', 'F&L'), ('B2C', 'B2C'), ('B2B', 'B2B'), ('OGE', 'OGE'), ('OGT', 'OGT'), ('OGV', 'OGV'), ('IGE', 'IGE'), ('IGT', 'IGT')], max_length=1, null=True)),
                ('leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
