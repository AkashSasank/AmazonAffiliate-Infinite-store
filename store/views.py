from django.shortcuts import render
from .constants import home_page_urls


# Create your views here.


def home(request):
    return render(template_name='home.html', request=request, context=home_page_urls)


def about(request):
    return render(template_name='home/about.html', request=request, context=home_page_urls)


def store(request):
    return render(template_name='store.html', request=request, context=home_page_urls)
