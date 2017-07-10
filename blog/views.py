from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Class


# Create your views here.


def blog_index(request):
    return render(request, 'blog/blog_index.html')


def load_sidebar():
    classes = Class.objects.filter(Status=1)
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
    page_dir = {
        'class_list': class_list,
        'class_tree_view_active': '',
        'now_class_id': None,
    }
    return page_dir


def blog_main(request):
    page_dir = load_sidebar()
    print page_dir
    return render(request, 'blog/blog_main.html', page_dir)


def blog_class(request, now_class_id):
    page_dir = load_sidebar()
    page_dir['class_tree_view_active'] = 'active'
    page_dir['now_class_id'] = int(now_class_id)
    print page_dir
    return render(request, 'blog/blog_class.html', page_dir)
