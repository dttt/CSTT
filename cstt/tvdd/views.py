from django.shortcuts import render
#from django.http import HttpResponse
from .forms import UserForm


def home(request):
    form = UserForm()
    return render(request, 'home.html', {'form': form})
