from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# when the /products is called it should point to the -> index function
# using the (Uniform Resource Locator) which means address


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')
