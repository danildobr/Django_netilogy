import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    
    current_time = str(datetime.datetime.now().time()).split('.')[0]
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files_list = os.listdir('.')
    response_content = "<h1>Список файлов в рабочей директории:</h1>"
    for file in files_list:
        response_content += f"<li>{file}</li>"
    
    return HttpResponse(response_content)
    
