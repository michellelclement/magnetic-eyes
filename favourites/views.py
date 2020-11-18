from django.shortcuts import render, redirect, reverse


def favourites(request):

    return render(request, 'favourites/favourites.html')


# Add items to Favourites
def add_to_favourites(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', {})

    favourites[item_id] = favourites

    request.session['favourites'] = favourites
    print(redirect_url)
    return redirect(reverse('product_detail', args=[item_id]))
