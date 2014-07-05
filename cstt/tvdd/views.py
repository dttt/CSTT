from django.shortcuts import render
#from django.http import HttpResponse
from .forms import UserForm
from helper.helper import Function, DishFunction
from helper.user import User


def home(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'home.html', {'form': form})
    else:
        #function = Function()
        function = DishFunction()
        data = request.POST
        user = User(data)
        dishes = function.get_menu(user=user)
        form = UserForm(data)
        return render(request, 'home.html', {
            'form': form, 'user': user, 'dishes': dishes}
        )


def test(request):
    #function = Function()
    form = UserForm(request.POST)
    return render(request, 'home.html', {'form': form})
