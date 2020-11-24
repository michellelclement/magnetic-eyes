from django.shortcuts import render
from products.models import Product


def index(request):

    products = Product.objects.order_by('-sku').all()[:2]
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def application(request):

    context = {
        'application_page': 'active',
    }

    return render(request, 'home/application.html', context)


def contact(request):

    context = {
        'contact_page': 'active',
    }

    return render(request, '/contact.html', context)


def about(request):

    return render(request, 'home', context)
