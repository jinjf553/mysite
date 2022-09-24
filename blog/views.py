# Create your views here.
from django.shortcuts import get_list_or_404, render

from .models import Post


def post_list(request):
    posts = Post.published_objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_list_or_404(Post, slug=post, status='published', publish__year=year,
                           publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
