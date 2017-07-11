from django.shortcuts import render
from blog.models import Class
from blog.models import Article


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
    sidebar_dir = {
        'class_list': class_list,
    }
    return sidebar_dir


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


def blog_main(request):
    sidebar_dir = load_sidebar()
    content_dir = load_content()
    return render(request, 'blog/blog_main.html', sidebar_dir, content_dir)


def blog_about_me(request):
    sidebar_dir = load_sidebar()
    sidebar_dir['about_me_active'] = 'active'
    return render(request, 'blog/blog_about_me.html', sidebar_dir)


def blog_time_line(request):
    sidebar_dir = load_sidebar()
    sidebar_dir['time_line_active'] = 'active'
    return render(request, 'blog/blog_time_line.html', sidebar_dir)


def blog_statistics(request):
    sidebar_dir = load_sidebar()
    sidebar_dir['statistics_active'] = 'active'
    return render(request, 'blog/blog_statistics.html', sidebar_dir)


def blog_class(request, now_class_id):
    sidebar_dir = load_sidebar()
    sidebar_dir['class_active'] = 'active'
    sidebar_dir['now_class_id'] = int(now_class_id)
    return render(request, 'blog/blog_class.html', sidebar_dir)


def blog_about_my_site(request):
    sidebar_dir = load_sidebar()
    sidebar_dir['about_my_site_active'] = 'active'
    return render(request, 'blog/blog_about_my_site.html', sidebar_dir)


def blog_article(request, now_article_id):
    sidebar_dir = load_sidebar()
    this_content_dir = load_one_article(now_article_id)
    # return render(request, 'blog/blog_article.html', sidebar_dir, this_content_dir)
    print this_content_dir['article_dir']['Content']
    return render(request, 'blog/blog_article.html', this_content_dir)
