from django.shortcuts import render

# Create your views here.

def favourites(request):

    return render(request, 'favourites/favourites.html')
