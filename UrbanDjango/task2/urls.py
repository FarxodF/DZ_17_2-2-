from django.urls import path
from .views import my_function_view, MyClassView

urlpatterns = [
    path('function/', my_function_view,
         name='function_view'),
    path('class/', MyClassView.as_view(),
         name='class_view'), ]
