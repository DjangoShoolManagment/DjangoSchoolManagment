from datetime import date

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    if request.method == 'POST':
        v_password = request.POST['password']
        if request.POST['is_staff'] == 1:
            v_is_staff = 1
            v_is_superuser = 0
        elif request.POST['is_staff'] == 2:
            v_is_staff = 0
            v_is_superuser = 1
        else:
            v_is_staff = 0
            v_is_superuser = 0
        v_username = request.POST['email']
        v_first_name = request.POST['first_name']
        v_last_name = request.POST['last_name']
        v_email = request.POST['email']
        v_is_active = 1
        v_date_joined = date.today()

        x = User.objects.create_user(password=v_password,
                                     is_superuser=v_is_superuser,
                                     username=v_username,
                                     first_name=v_first_name,
                                     last_name=v_last_name,
                                     email=v_email,
                                     is_staff=v_is_staff,
                                     is_active=v_is_active,
                                     date_joined=v_date_joined)
        x.save()
        print('Registration is completed')
        return redirect('/')
    else:
        return render(request, 'signup.html', {'title': 'Sign Up'})


def login(request):
    return redirect('/')

# if request.method == 'POST' and 'btnRegister' in request.POST: return redirect('/login/')
