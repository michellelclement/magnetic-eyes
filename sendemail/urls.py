from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path('email/', contactView, name='email'),
    path('success/', successView, name='success'),
]