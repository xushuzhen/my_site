from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Class
from blog.models import Article
from blog.models import Lable

# Create your views here.
page_size = 8


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
    }
    return page_dir


def load_content():
    articles = Article.objects.filter(Status=1)
    article_list = []
    for each_article in articles:
        article_dir = {
            'ArticleID': each_article.ArticleID,
            'DescriptionSEO': each_article.DescriptionSEO,
            'KeywordsSEO': each_article.KeywordsSEO,
            'AuthorSEO': each_article.AuthorSEO,
            'Title': each_article.Title,
            'Content': each_article.Content,
            'Class': each_article.Class,
            'Lable': each_article.Lable,
            'PageView': each_article.PageView,
            'Status': each_article.Status,
            'CreateTime': each_article.CreateTime,
            'UpdateTime': each_article.UpdateTime,
        }
        article_list.append(article_dir)
    content_dir = {
        'article_list': article_list,
    }
    return content_dir


def load_one_article(now_article_id):
    each_article = Article.objects.get(ArticleID=now_article_id, Status=1)
    temp_article_dir = {
        'ArticleID': each_article.ArticleID,
        'DescriptionSEO': each_article.DescriptionSEO,
        'KeywordsSEO': each_article.KeywordsSEO,
        'AuthorSEO': each_article.AuthorSEO,
        'Title': each_article.Title,
        'Content': each_article.Content,
        'Class': each_article.Class,
        'Lable': each_article.Lable,
        'PageView': each_article.PageView,
        'Status': each_article.Status,
        'CreateTime': each_article.CreateTime,
        'UpdateTime': each_article.UpdateTime,
    }
    article_dir = {
        'article_dir': temp_article_dir,
    }
    return article_dir


def load_turn_page(page_type, now_page, type_parem=None):
    now_page = int(now_page)
    article_count = 0
    page_count = 0
    content_list = None
    pages_show = None

    if page_type == 'order_main_page':
        article_count = Article.objects.filter(Status=1).count()
        content_list = Article.objects.filter(Status=1).order_by('-CreateTime')[(now_page - 1) * 8: now_page * 8]
    elif page_type == 'order_class_page':
        article_count = Article.objects.filter(Status=1, Class=type_parem).count()
        content_list = Article.objects.filter(Status=1, Class=type_parem).order_by('-CreateTime')[
                       (now_page - 1) * 8: now_page * 8]
    temp_page_count = divmod(article_count, page_size)
    if temp_page_count[1] != 0:
        page_count = temp_page_count[0] + 1
    else:
        page_count = temp_page_count[0]

    article_list = []
    for each_article in content_list:
        article_dir = {
            'ArticleID': each_article.ArticleID,
            'DescriptionSEO': each_article.DescriptionSEO,
            'KeywordsSEO': each_article.KeywordsSEO,
            'AuthorSEO': each_article.AuthorSEO,
            'Title': each_article.Title,
            'Content': each_article.Content,
            'Class': each_article.Class,
            'Lable': each_article.Lable,
            'PageView': each_article.PageView,
            'Status': each_article.Status,
            'CreateTime': each_article.CreateTime,
            'UpdateTime': each_article.UpdateTime,
        }
        class_id_list = article_dir['Class'].split(',')
        class_name_list = []
        for each_class in class_id_list:
            class_name_list.append(Class.objects.get(ClassID=int(each_class)).ClassName)
        lable_id_list = article_dir['Lable'].split(',')
        lable_name_list = []
        for each_lable in lable_id_list:
            lable_name_list.append(Lable.objects.get(LableID=int(each_lable)).LableName)
        article_dir['class_id_list'] = class_id_list
        article_dir['class_name_list'] = class_name_list
        article_dir['lable_id_list'] = lable_id_list
        article_dir['lable_name_list'] = lable_name_list
        article_list.append(article_dir)

    if page_count < 7:
        pages_show = [x for x in range(1, page_count + 1)]
    elif page_count - now_page == 2:
        pages_show = [now_page - 4, now_page - 3, now_page - 2, now_page - 1, now_page, now_page + 1, now_page + 2]
    elif page_count - now_page == 1:
        pages_show = [now_page - 5, now_page - 4, now_page - 3, now_page - 2, now_page - 1, now_page, now_page + 1]
    elif page_count == now_page:
        pages_show = [now_page - 6, now_page - 5, now_page - 4, now_page - 3, now_page - 2, now_page - 1, now_page]
    else:
        pages_show = [now_page - 3, now_page - 2, now_page - 1, now_page, now_page + 1, now_page + 2, now_page + 3]

    previous_page_num = now_page
    next_page_num = now_page
    if now_page != 1:
        previous_page_num = now_page - 1
    if now_page != page_count:
        next_page_num = now_page + 1

    content_dir = {
        'article_list': article_list,
        'page_count': page_count,
        'pages_show': pages_show,
        'now_page': now_page,
        'previous_page_num': previous_page_num,
        'next_page_num': next_page_num,
    }
    return content_dir


def blog_redirect(request):
    return HttpResponseRedirect('/blog/1/')


def blog_main(request, now_page):
    page_dir = load_sidebar()
    content_dir = load_turn_page('order_main_page', now_page)
    page_dir.update(content_dir)
    return render(request, 'blog/blog_main.html', page_dir)


def blog_about_me(request):
    page_dir = load_sidebar()
    page_dir.update({
        'about_me_active': 'active',
    })
    return render(request, 'blog/blog_about_me.html', page_dir)


def blog_time_line(request):
    page_dir = load_sidebar()
    page_dir.update({
        'time_line_active': 'active',
    })
    return render(request, 'blog/blog_time_line.html', page_dir)


def blog_statistics(request):
    page_dir = load_sidebar()
    page_dir.update({
        'statistics_active': 'active',
    })
    return render(request, 'blog/blog_statistics.html', page_dir)


def blog_class(request, now_class_id):
    page_dir = load_sidebar()
    page_dir.update({
        'class_active': 'active',
        'now_class_id': int(now_class_id),
    })
    return render(request, 'blog/blog_class.html', page_dir)


def blog_about_my_site(request):
    page_dir = load_sidebar()
    page_dir.update({
        'about_my_site_active': 'active',
    })
    return render(request, 'blog/blog_about_my_site.html', page_dir)


def blog_article(request, now_article_id):
    page_dir = load_sidebar()
    this_content_dir = load_one_article(now_article_id)
    # return render(request, 'blog/blog_article.html', sidebar_dir, this_content_dir)
    print this_content_dir['article_dir']['Content']
    return render(request, 'blog/blog_article.html', this_content_dir)
