from django.urls import path
from . import views
from .views import index, shop, cart, Menu

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('menu/', Menu.as_view(), name='menu')
]
