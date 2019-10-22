from django.forms import ModelForm

from meetings.models import Meeting


class MeetingForm(ModelForm):

    class Meta:
        model = Meeting
        fields = ('type', 'date', 'time', 'participants')

class MeetingFormWithLeader(ModelForm):

    class Meta:
        model = Meeting
        fields = ('type', 'date', 'time', 'leader', 'participants')