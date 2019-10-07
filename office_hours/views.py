
from datetime import datetime, date

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from office_hours.models import OfficeHour


def check(request):
    return render(request, 'office_hours/check.html', {'request_user': request.user})


def checkin(request):
    if request.user.is_working:
        return HttpResponse("Você já está fazendo office hour :)")
    else:
        officehour = OfficeHour.objects.create(member=request.user)
        officehour.save()
        request.user.is_working = True
        request.user.save()
        return redirect('office_hours_history')
    return render(request, {'request_user': request.user})


def checkout(request):
    if request.user.is_working:
        officehour = OfficeHour.objects.get(member=request.user, checkout_time__isnull=True)
        officehour.checkout_time = timezone.now()
        print(officehour.checkout_time)
        duration = datetime.combine(date.min, officehour.checkout_time) - datetime.combine(date.min, officehour.checkin_time)
        officehour.duration = duration
        officehour.save()
        request.user.is_working = False
        request.user.save()
        return redirect('office_hours_history')
    else:
        return HttpResponse("Você precisa fazer check in antes :)")
    return render(request, 'office_hours/history.html', {'request_user': request.user})


def history(request):
    office_hours = OfficeHour.objects.filter(member=request.user)
    return render(request, 'office_hours/history.html', {'office_hours': office_hours, 'request_user': request.user})
