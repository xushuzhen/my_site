from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def blog(request):
    return render(request, 'blog/blog_base.html')
