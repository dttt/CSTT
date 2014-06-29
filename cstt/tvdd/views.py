from django.shortcuts import render
#from django.http import HttpResponse
from .forms import UserForm
from helper.helper import Function
from helper.user import User


def home(request):
    if request.GET:
        form = UserForm()
        return render(request, 'home.html', {'form': form})
    else:
        #function = Function()
        data = request.POST
        user = User(data)
        form = UserForm(data)
        return render(request, 'home.html', {'form': form, 'user': user})


def test(request):
    #function = Function()
    form = UserForm(request.POST)
    return render(request, 'home.html', {'form': form})
