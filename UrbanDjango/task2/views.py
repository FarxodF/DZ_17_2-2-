from django.shortcuts import render
from django.views.generic import TemplateView


def my_function_view(request):
    return render(request, 'second_task/function_view_template.html')


class MyClassView(TemplateView):
    template_name = 'second_task/class_view_template.html'


