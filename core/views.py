from django.shortcuts import render
from django.views.generic import CreateView
from products.models import Product

# Create your views here.

def home (request):
    return render(request, 'core/index.html')


def about (request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

# def menu (request):
#     return render(request, 'core/menu.html')

def service(request):
    return render(request, 'core/service.html')

# def team (request):
#     return render(request, 'core/team.html')

def testimonial (request):
    return render(request, 'core/testimonial.html')

