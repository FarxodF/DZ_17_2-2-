from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PUBG MOBILE']
    }
    return render(request, 'fourth_task/shop.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')


class Menu(TemplateView):
    template_name = 'fourth_task/menu.html'
