from django.shortcuts import render, redirect
from meetings.forms import MeetingForm, MeetingFormWithLeader, ParticipationForm

# Create your views here.
from meetings.models import Meeting, Participation


def new_meeting(request):
    registered = False
    if request.method == 'POST':
        meeting = Meeting.objects.create(leader=request.user)
        participation1 = Participation.objects.create(meeting=meeting)
        participation2 = Participation.objects.create(meeting=meeting)
        meeting_form = MeetingForm(request.POST or None, instance=meeting)
        participation_form1 = ParticipationForm(request.POST or None, instance=participation1)
        participation_form2 = ParticipationForm(request.POST or None, instance=participation2)
        if meeting_form.is_valid():
            meeting = meeting_form.save()
            participation1 = participation_form1.save()
            participation2 = participation_form2.save()
            registered = True
        else:
            print(meeting_form.errors)
    else:
        meeting_form = MeetingForm()
        participation_form1 = ParticipationForm()
        participation_form2 = ParticipationForm()
    return render(request, 'meeting/new_meeting.html',
                  {'meeting_form': meeting_form,
                   'participation_form1': participation_form1,
                   'participation_form2': participation_form2,
                   'registered': registered,
                   'request_user': request.user})


def my_meetings(request):
    meetings = Meeting.objects.filter(leader=request.user).order_by('-date')
    return render(request, 'meeting/my_meetings.html', {'meetings': meetings, 'request_user': request.user})


def meetings_list(request):
    meetings = Meeting.objects.all().order_by('-date')
    return render(request, 'meeting/meetings_list.html',
                  {'meetings': meetings, 'request_user': request.user})



def meeting_edit(request, id):
    meeting = Meeting.objects.get(id=id)
    form = MeetingFormWithLeader(request.POST or None, instance=meeting)
    if form.is_valid():
        form.save()
        return redirect('meeting_list')
    return render(request, 'meeting/meeting_edit.html', {'form': form, 'request_user': request.user})


def meeting_delete(request, id):
    meeting = Meeting.objects.get(id=id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meeting_list')
    return render(request, 'meeting/meeting_confirm_delete.html', {'meeting': meeting, 'request_user': request.user})
