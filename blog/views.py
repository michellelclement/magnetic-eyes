from django.shortcuts import render
from django.views import generic
from .models import Post


def all_posts(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    template = "blog/blog.html"
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


