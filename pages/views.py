from django.shortcuts import render
# Create your views here.

# Ultimately we want to render a template for the home page
# but for now we will just temporarily import HttpResponse

# This is temporary
from django.http import HttpResponse
# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')

# We want to render a template instead of a dummy HttpResponse.
# To tell Django where to look for we will go to btre > settings.py and add template there in the 'DIRS'


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
