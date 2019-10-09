
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from office_hours.forms import OfficeHourForm
from office_hours.models import OfficeHour

@login_required
def check(request):
    timenow = timezone.now()
    return render(request, 'office_hours/check.html', {'request_user': request.user, 'timenow': timenow})

@login_required
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

@login_required
def checkout(request):
    if request.user.is_working:
        officehour = OfficeHour.objects.get(member=request.user, checkout_time__isnull=True)
        officehour.checkout_time = timezone.now()
        officehour.duration = officehour.checkout_time - officehour.checkin_time
        officehour.save()
        request.user.is_working = False
        request.user.save()
        return redirect('office_hours_history')
    else:
        return HttpResponse("Você precisa fazer check in antes :)")
    return render(request, 'office_hours/myhistory.html', {'request_user': request.user})

@login_required
def myhistory(request):
    office_hours = OfficeHour.objects.filter(member=request.user).order_by('-checkin_time')
    return render(request, 'office_hours/myhistory.html', {'office_hours': office_hours, 'request_user': request.user})

@login_required
def officehour_list(request):
    office_hours = OfficeHour.objects.all().order_by('-checkin_time')
    return render(request, 'office_hours/officehour_list.html', {'office_hours': office_hours, 'request_user': request.user})

@login_required
def officehour_update(request, id):
    officehour = OfficeHour.objects.get(id=id)
    form = OfficeHourForm(request.POST or None, instance=officehour)
    if form.is_valid():
        form.save()
        return redirect('officehours_list')
    return render(request, 'office_hours/officehour_update.html', {'form': form, 'request_user': request.user})

@login_required
def officehour_delete(request, id):
    officehour = OfficeHour.objects.get(id=id)
    if request.method == 'POST':
        officehour.delete()
        return redirect('officehours_list')
    return render(request, 'office_hours/officehour_confirm_delete.html', {'officehour': officehour, 'request_user': request.user})

