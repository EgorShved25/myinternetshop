from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout # Аутефикация в джанго
from django.contrib import messages # выходят сообщения на экран при регистрации


def home(request):
    products = Product.objects.all() # добовляем модель продукта и присваем ему имя products
    return render(request, 'home.html', {'products':products}) # передаем products внутрь шаблона

def about(request):
    return render(request, 'about.html')

def about_shop(request):
    return render(request, 'about_shop.html')


def login_user(request): # регистрация пользователя
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Cool!!'))
            return redirect('home')
        else:
            messages.success(request, ('Cool!!'))
            return redirect('login')

    else:
        return render(request, 'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home') # redirect перенаправляет на страницу home.html


