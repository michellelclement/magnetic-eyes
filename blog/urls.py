from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
