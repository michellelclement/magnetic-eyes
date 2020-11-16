from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def application(request):
    return render(request, 'home/application.html')

def contact(request):
    return render(request, '/contact.html')

def about(request):
    return render(request, 'home')
