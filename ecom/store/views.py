from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all() # добовляем модель продукта и присваем ему имя products
    return render(request, 'home.html', {'products':products}) # передаем products внутрь шаблона

def about(request):
    return render(request, 'about.html')

def about_shop(request):
    return render(request, 'about_shop.html')


def about_shop(request):
    return render(request, 'about_shop.html')



