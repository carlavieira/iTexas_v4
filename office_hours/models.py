from django.db import models

from members.models import MyUser


class OfficeHour(models.Model):
    member = models.ForeignKey('MyUser', on_delete=models.CASCADE, verbose_name='Membro'),
    date = models.DateField(verbose_name='Dia', auto_now_add=True, ),
    checkin_time = models.TimeField(verbose_name='Hora do check-in', auto_now_add=True),
    checkout_time = models.TimeField(verbose_name='Hora do check-out', default=''),
    duration = models.DurationField(verbose_name='Duração')

    def __str__(self):
        return self.pk
