# mysite/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world! This site is Created by Micky Kumar')

