from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog/showblogs.html", {'blogs': blogs})


def details(request, blog_id):
    blog_details = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog/details.html", {'blog_details': blog_details})