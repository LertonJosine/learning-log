from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth.views import LoginView


# Create your views here.

def my_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def registrar(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            autenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, autenticated_user)
            return HttpResponseRedirect(reverse('topics'))
    context = {'form':form}
    return render(request, 'registration/register.html', context)


def my_login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticaded_user = authenticate(username=request.POST["username"], password=request.POST["password"])
            login(request, authenticaded_user)
            return HttpResponseRedirect(reverse('topics'))
    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context)