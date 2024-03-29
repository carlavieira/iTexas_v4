from django import forms
from django.forms import ModelForm

from office_hours.models import OfficeHour


class OfficeHourForm(ModelForm):

    class Meta:
        model = OfficeHour
        fields = ('checkin_time', 'checkout_time')
