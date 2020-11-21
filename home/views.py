from django.shortcuts import render
from products.models import Product


def index(request):
    return render(request, 'home/index.html')


def application(request):
    return render(request, 'home/application.html')


def contact(request):
    return render(request, '/contact.html')


def about(request):
    return render(request, 'home')


def products(request):

    products = Products.objects.all()
    context = {
        'products': products,
    }

    return render(request, context)
