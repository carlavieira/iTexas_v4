from django.shortcuts import render, redirect
from meetings.forms import MeetingForm, MeetingFormWithLeader

# Create your views here.
from meetings.models import Meeting


def new_meeting(request):
    registered = False
    if request.method == 'POST':
        meeting = Meeting.objects.create(leader=request.user)
        meeting_form = MeetingForm(request.POST or None, instance=meeting)
        if meeting_form.is_valid():
            meeting = meeting_form.save()
            registered = True
        else:
            print(meeting_form.errors)
    else:
        meeting_form = MeetingForm()
    return render(request, 'meeting/new_meeting.html',
                  {'meeting_form': meeting_form,
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
