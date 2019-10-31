from django.shortcuts import render, redirect
from events.forms import EventForm, EventFormWithLeader
# Create your views here.
from events.models import Event

def new_event(request):
    registered = False
    if request.method == 'POST':
        event = Event.objects.create(leader=request.user)
        event_form = EventForm(request.POST or None, instance=event)
        if event_form.is_valid():
            event = event_form.save()
            registered = True
        else:
            print(event_form.errors)
    else:
        event_form = EventForm()
    return render(request, 'event/new_event.html',
                  {'event_form': event_form,
                   'registered': registered,
                   'request_user': request.user})