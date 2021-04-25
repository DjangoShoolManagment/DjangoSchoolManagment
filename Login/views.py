from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def login_user(request):
    logout(request)

    username = password = ''
    if request.GET:
        cookies_get_user = request.COOKIES['cUser']
        cookies_get_pwd = request.COOKIES['cPwd']

    if request.POST:
        username = request.POST['txtUser']
        password = request.POST['txtPwd']
        response = HttpResponse()
        response.set_cookie('cUser', request.POST['txtUser'])
        response.set_cookie('cPwd', request.POST['txtPwd'])
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                UserData = request.user.first_name + ' ' + request.user.last_name
                return render(request, 'Adminindex.html', {'school': 'Donbosco', 'UserData': UserData})
                #return redirect('/adminindex/')
            else:
                return render(request, 'ErrorPage.html', {'error': 'User is not Active', 'errorno': '401'})
        else:

            return render(request, 'ErrorPage.html', {'error': 'Invalid login details', 'errorno': '402'})
    else:
        # return render_to_response('login.html', context_instance=RequestContext(request))
        return render(request, 'login.html', {'school': 'Donbosco'})


@login_required(login_url='/')
def adminindex(request):
    return render(request, 'Adminindex.html', {'school': 'Donbosco'})


def errorpage(request):
    return render(request, 'ErrorPage.html', {'school': 'Donbosco'})
