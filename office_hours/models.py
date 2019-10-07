from datetime import date

from django.db import models
from django.utils import timezone

from members.models import MyUser


class OfficeHour(models.Model):
    member = models.ForeignKey(MyUser, verbose_name='Membro', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Dia', default=date.today)
    checkin_time = models.TimeField(verbose_name='Hora do check-in', default=timezone.now)
    checkout_time = models.TimeField(verbose_name='Hora do check-out', blank=True, null=True)
    duration = models.DurationField(verbose_name='Duração', blank=True, null=True)

