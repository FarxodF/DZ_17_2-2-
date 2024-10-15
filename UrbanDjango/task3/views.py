from django.shortcuts import render
import UrbanDjango.urls


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    products = {
        'product1': 'Game 1',
        'product2': 'Game 2',
        'product3': 'Game 3',
    }
    context = {'products': products}
    return render(request, 'third_task/shop.html', context)


def cart(request):
    context = {'message': 'Ваша корзина пуста.'}
    return render(request, 'third_task/cart.html', context)
