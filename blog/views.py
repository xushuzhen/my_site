from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Class


# Create your views here.


def blog_index(request):
    return render(request, 'blog/blog_index.html')


def load_class():
    classes = Class.objects.filter(Status=1)
    page_dir = {}
    class_list = []
    for each_class in classes:
        class_dir = {
            'ClassID': each_class.ClassID,
            'ClassName': each_class.ClassName,
            'ClassAbstract': each_class.ClassAbstract,
            'Status': each_class.Status,
            'CreateTime': each_class.CreateTime,
            'UpdateTime': each_class.UpdateTime,
        }
        class_list.append(class_dir)
    page_dir['class_list'] = class_list
    return page_dir


def blog_main(request):
    page_dir = load_class()
    return render(request, 'blog/blog_main.html', page_dir)


def blog_class(request, class_id):
    page_dir = load_class()
    return render(request, 'blog/blog_class.html', page_dir)
