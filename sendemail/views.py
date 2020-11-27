from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from profiles.models import UserProfile


def contactView(request):

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = ContactForm(initial={
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            form = ContactForm()
    else:
        form = ContactForm()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['michellelclement@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    context = {
        'contact_page': 'active',
        'form': form,
    }

    return render(request, "sendemail/contact.html", context)


def successView(request):

    return render(request, "sendemail/contact_success.html")
