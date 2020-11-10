from django.shortcuts import render


# Display User Profile
def profile(request):
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
