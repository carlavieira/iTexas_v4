from django.db import models

from members.models import MyUser


class OfficeHour(models.Model):
    member = models.ForeignKey("MyUser", on_delete=models.CASCADE, verbose_name='Membro'),
    date = models.DateField(verbose_name='Dia', auto_now_add=True, ),
    checkin_time = models.TimeField,
    checkout_time = models.TimeField,
    duration = models.DurationField(),
