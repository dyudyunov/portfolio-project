from django.shortcuts import render, get_object_or_404

from .models import Blog
# Create your views here.

def all_posts(request):
    blogs = Blog.objects
    return render(request, 'blog/all_posts.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})