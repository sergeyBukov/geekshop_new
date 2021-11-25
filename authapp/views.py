
from django.shortcuts import render

# Create your views here.
from authapp.forms import UserLoginForm

def login(request):
    context = {
        'title': 'Geekshop | Авторизация',
        'form': UserLoginForm()
        }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {
        'title': 'Geekshop | Регистрация', }
    return render(request, 'authapp/register.html', context)
