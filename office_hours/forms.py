from django.forms import forms

from office_hours.models import OfficeHour


class OfficeHourForm(forms.ModelForm):
    class Meta:
        model = OfficeHour
        fields = ('date', 'checkin_time', 'checkout_time')
