import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.models import MyUser
from office_hours.forms import OfficeHourForm
from office_hours.models import OfficeHour


def check(request):
    return render(request, 'office_hours/check.html', {'request_user': request.user})


def checkin(request):
    user = MyUser.objects.get(id=request.user.id)
    if user.is_working:
        return HttpResponse("Você já está fazendo office hour :)")
    else:
        officehour = OfficeHour
        officehour.checkin_time = datetime.datetime.now().strftime('%H:%M:%S')
        officehour.date = datetime.datetime.now().strftime('%DD/%MM/%YY')
        officehour.save()
        user.is_working = True
        return redirect('office_hours_history')
    return render(request, 'office_hours/history.html', {'request_user': request.user})


def checkout(request):
    user = MyUser.objects.get(user=request.user)
    if user.is_working:
        today = datetime.datetime.now().strftime('%DD/%MM/%YY')
        officehour = OfficeHour.objects.get(member=request.user, checkout="", date=today)
        officehour.checkout_time = datetime.datetime.now().strftime('%H:%M:%S')
        officehour.duration = officehour.checkout_time - officehour.checkin_time
        officehour.save()
        user.is_working = False
        return redirect('office_hours_history')
    else:
        return HttpResponse("Você precisa fazer check in antes :)")
    return render(request, 'office_hours/history.html', {'request_user': request.user})


def history(request):
    office_hours = OfficeHour.objects.get(member=request.user)
    return render(request, 'office_hours/history.html', {'request_user': request.user, 'office_hours': office_hours})
