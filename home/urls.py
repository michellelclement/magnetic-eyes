from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('application/', views.application, name='application'),
    path('', views.index, name='about'),
]
