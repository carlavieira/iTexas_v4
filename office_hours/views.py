from django.shortcuts import render

from office_hours.models import OfficeHour


def check(request):
    return render(request, 'office_hours/check.html', {'request_user': request.user})


def checkin(request):
    return render(request, 'registration.html',
                  {'request_user': request.user})
