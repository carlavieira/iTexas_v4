from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from members.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from members.models import MyUser


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['profile_pic']
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        podio_code = request.POST.get('podio_code')
        password = request.POST.get('password')
        user = authenticate(podio_code=podio_code, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(podio_code, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user_login.html', {})


def member_list(request, template_name='members/member_list.html'):
    user = MyUser.objects.all()
    data = {}
    data['object_list'] = user
    return render(request, template_name, data)


def member_view(request, pk, template_name='members/member_detail.html'):
    user = get_object_or_404(MyUser, pk=pk)
    return render(request, template_name, {'object': user})


def member_update(request, pk, template_name='members/member_form.html'):
    user = get_object_or_404(MyUser, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, template_name, {'form': form})


def member_delete(request, pk, template_name='members/member_confirm_delete.html'):
    user = get_object_or_404(MyUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('member_list')
    return render(request, template_name, {'object': user})


def member_view(request, pk, template_name='members/member_detail.html'):
    user = get_object_or_404(MyUser, pk=pk)
    return render(request, template_name, {'object': user})
