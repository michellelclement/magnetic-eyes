from django.shortcuts import render, redirect


def favourites(request):

    return render(request, 'favourites/favourites.html')


# Add items to Favourites
def add_to_favourites(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', {})

    favourites[item_id] = favourites

    request.session['favourites'] = favourites
    print(request.session['favourites'])
    return redirect(redirect_url)
