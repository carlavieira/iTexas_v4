from django.forms import ModelForm

from meetings.models import Meeting, Participation


class MeetingForm(ModelForm):

    class Meta:
        model = Meeting
        fields = ('type', 'date', 'time' )

class MeetingFormWithLeader(ModelForm):

    class Meta:
        model = Meeting
        fields = ('type', 'date', 'time', 'leader')

class ParticipationForm(ModelForm):

    class Meta:
        model = Participation
        fields = ('member', 'present')