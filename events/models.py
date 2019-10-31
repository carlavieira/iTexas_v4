from django.db import models
from datetime import date

# Create your models here.
from django.utils import timezone
from members.models import MyUser


class Event(models.Model):
    MEETINGS = (('RG', 'Reunião Geral'), ('AS', 'Assembléia'))
    type = models.CharField(max_length=3, choices=MEETINGS, blank=True, null=True, verbose_name='Tipo do Evento')
    leader = models.ForeignKey(MyUser, verbose_name='Líder', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Dia', default=date.today)
    time = models.TimeField(verbose_name='Hora', default=timezone.now)

    def __str__(self):
        return "%s do %s" % (self.type, self.leader.first_name)
