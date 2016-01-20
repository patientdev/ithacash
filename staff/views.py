from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from .forms import StaffLogin, StaffSignup
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from accounts.models import IthacashUser
from staff.models import IthacashStaff


def login_staff(request):
    form = StaffLogin(request.POST or None)

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/staff/{:d}/'.format(user.id))

            else:
                return JsonResponse({'fail': True}, status=400)
        else:
            return JsonResponse({'fail': True}, status=404, reason="BAD REQUEST: User does not exist")

    else:
        return render(request, 'login.html', {'form': form})


def signup(request):
    form = StaffSignup(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            user = form.save()

            return JsonResponse({'success': True}, status=202, reason="OK: Form values accepted")

        else:
            return JsonResponse(form.errors, status=400)

    return render(request, 'signup.html', {'form': form})


def dashboard(request, staff_id):

    if request.user.is_authenticated():

        if int(staff_id) != request.user.id:
            return HttpResponseRedirect('/staff/{:d}/'.format(request.user.id))

        return render(request, 'dashboard.html', {'ithacash_users': IthacashUser.objects.all()})

    else:
        HttpResponseRedirect('/')
