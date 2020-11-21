from django.shortcuts import render
from products.models import Product


def index(request):

    products = Product.objects.order_by('-sku').all()[:2]
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def application(request):
    return render(request, 'home/application.html')


def contact(request):
    return render(request, '/contact.html')


def about(request):
    return render(request, 'home')
