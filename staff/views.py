from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from .forms import StaffLogin, StaffSignup
from django.contrib.auth import login, authenticate

from accounts.models import IthacashUser
from staff.models import IthacashStaff

from django.utils.timezone import now
from datetime import timedelta


def staff_front(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/staff/dashboard/')

    else:
        return HttpResponseRedirect('/staff/login/')


def login_staff(request):
    form = StaffLogin(data=request.POST or None)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(username=username, password=password)
        except:
            user = None

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/staff/dashboard/')

            else:
                return render(request, 'staff/login.html', {'form': form})
        else:
            return render(request, 'staff/login.html', {'form': form})

    elif request.user.is_authenticated():
        return HttpResponseRedirect('/staff/dashboard/')

    else:
        return render(request, 'staff/login.html', {'form': form})


def signup(request):
    form = StaffSignup(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            user = form.save()
            user.send_confirmation_message()

            return JsonResponse({'success': True}, status=202, reason="OK: Form values accepted")

        else:
            return JsonResponse(form.errors, status=400)

    elif request.user.is_authenticated():
        return HttpResponseRedirect('/staff/dashboard/')

    else:
        return render(request, 'staff/signup.html', {'form': form})


def dashboard(request):

    if request.user.is_authenticated():

        last_week = now() - timedelta(days=7)

        return render(request, 'staff/dashboard.html', {'ithacash_users': IthacashUser.objects.filter(accounts__created__gt=last_week)})

    else:
        return HttpResponseRedirect('/staff/login/')
