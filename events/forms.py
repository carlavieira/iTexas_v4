from django.forms import ModelForm

from events.models import Event


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ('type', 'date', 'time' )

class EventFormWithLeader(ModelForm):

    class Meta:
        model = Event
        fields = ('type', 'date', 'time', 'leader')
