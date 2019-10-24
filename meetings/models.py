from django.db import models
from datetime import date

# Create your models here.
from django.utils import timezone
from members.models import MyUser


class Meeting(models.Model):
    MEETINGS = (('REB', 'REB'), ('RA', 'Reunião de Área'), ('RT', 'Reunião de Time'), ('LR', 'Reunião de LR'),
                ('CN', 'Reunião de Corner'))
    type = models.CharField(max_length=3, choices=MEETINGS, blank=True, null=True, verbose_name='Tipo da Reunião')
    leader = models.ForeignKey(MyUser, verbose_name='Líder', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Dia', default=date.today)
    time = models.TimeField(verbose_name='Hora', default=timezone.now)

    def __str__(self):
        return "%s do %s" % (self.type, self.leader.first_name)

class Participation(models.Model):
    present = models.BooleanField(default=False)
    member = models.ForeignKey(MyUser, verbose_name='Participante', on_delete=models.CASCADE, null=True)
    meeting = models.ForeignKey(Meeting, verbose_name='Reunião', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.member.first_name, self.present)
