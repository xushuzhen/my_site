# coding: utf-8
import logging
import jieba
import random
import json
import uuid
import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import Class
from blog.models import Article
from blog.models import Label

# Create your views here.
page_size = 10


def get_date_range():
    now_date = datetime.datetime.now()
    flag_year = now_date.year
    flag_month = now_date.month
    temp_year = 0
    temp_month = 0
    date_range = []
    for i in range(0, 12):
        if flag_month == 12:
            temp_year = flag_year + 1
            temp_month = 1
        else:
            temp_year = flag_year
            temp_month = flag_month + 1
        date_range.append([flag_year, flag_month, 1, temp_year, temp_month, 1])
        if i == 11:
            break
        if flag_month == 1:
            flag_year = flag_year - 1
            flag_month = 12
        else:
            flag_month = flag_month - 1
    date_range.append([2016, 1, 1, flag_year, flag_month, 1])
    return date_range


def get_article_class_list(class_id_list):
    class_name_list = {}
    for each_class in class_id_list:
        class_name_list[each_class] = Class.objects.get(ClassID=int(each_class)).ClassName
    return class_name_list


def get_article_lable_list(label_id_list):
    label_name_list = []
    for each_label in label_id_list:
        label_name_list.append(Label.objects.get(LabelID=int(each_label)).LabelName)
    return label_name_list


def load_sidebar():
    classes = Class.objects.filter(Status=1)
    class_list = []
    for each_class in classes:
        article_count = Article.objects.filter(Class=each_class.ClassID).count()
        class_dir = {
            'ClassID': each_class.ClassID,
            'ClassName': each_class.ClassName,
            'ClassArticleCount': article_count,
            'ClassAbstract': each_class.ClassAbstract,
            'Status': each_class.Status,
            'CreateTime': each_class.CreateTime,
            'UpdateTime': each_class.UpdateTime,
        }
        class_list.append(class_dir)
    top_article_list = []
    articles = Article.objects.filter(Status=1).order_by('-PageView')[:10]
    for each_article in articles:
        temp_title = each_article.Title
        if len(each_article.Title) > 10:
            temp_title = each_article.Title[:10] + '...'
        article_dir = {
            'ArticleID': each_article.ArticleID,
            'Title': temp_title,
            'PageView': each_article.PageView,
        }
        top_article_list.append(article_dir)

    range_list = []
    date_range = get_date_range()
    for each_range in date_range:
        start_date = datetime.date(each_range[0], each_range[1], each_range[2])
        end_date = datetime.date(each_range[3], each_range[4], each_range[5])
        range_count = Article.objects.filter(Status=1, CreateTime__range=(start_date, end_date)).count()
        range_dir = {
            'range_path': '%s-%s-%s-%s-%s-%s' % (
                each_range[0], each_range[1], each_range[2], each_range[3], each_range[4], each_range[5]
            ),
            'range_count': range_count,
            'range_date': '%s年%s月' % (each_range[0], each_range[1])
        }
        range_list.append(range_dir)
    range_list[-1]['range_date'] = '更多'
    sidebar_dir = {
        'class_list': class_list,
        'top_article_list': top_article_list,
        'range_list': range_list,
    }
    return sidebar_dir


def load_one_article(now_article_id, now_article_status=1):
    each_article = None
    if now_article_status == 1:
        each_article = Article.objects.get(ArticleID=now_article_id, Status=1)
    else:
        each_article = Article.objects.get(ArticleID=now_article_id)
    temp_article_dir = {
        'ArticleID': each_article.ArticleID,
        'DescriptionSEO': each_article.DescriptionSEO,
        'KeywordsSEO': each_article.KeywordsSEO,
        'AuthorSEO': each_article.AuthorSEO,
        'Title': each_article.Title,
        'Content': each_article.Content,
        'Class': each_article.Class,
        'Label': each_article.Label,
        'PageView': each_article.PageView,
        'Status': each_article.Status,
        'TimeLine': each_article.TimeLine,
        'TimeLineType': each_article.TimeLineType,
        'CreateTime': each_article.CreateTime.strftime('%Y年%m月%d日 %H:%M:%S'),
        'UpdateTime': each_article.UpdateTime.strftime('%Y年%m月%d日 %H:%M:%S'),
    }
    article_dir = {
        'this_article': temp_article_dir,
    }
    return article_dir


def load_turn_page(page_type, now_page, type_parem=None):
    now_page = int(now_page)
    article_count = 0
    page_count = 0
    content_list = None
    pages_show = None
    page_type_href = None
    # page_type_href_head = '/blog'
    page_type_href_head = ''

    if page_type == 'order_main_page':
        page_type_href = '%s' % (page_type_href_head)
        article_count = Article.objects.filter(Status=1).count()
        content_list = Article.objects.filter(Status=1).order_by('-CreateTime')[
                       (now_page - 1) * page_size: now_page * page_size]
    elif page_type == 'order_class_page':
        page_type_href = '%s/class/%s' % (page_type_href_head, type_parem)
        article_count = Article.objects.filter(Status=1, Class=type_parem).count()
        content_list = Article.objects.filter(Status=1, Class=type_parem).order_by('-CreateTime')[
                       (now_page - 1) * page_size: now_page * page_size]
    elif page_type == 'order_date_page':
        page_type_href = '%s/article_range/%s' % (page_type_href_head, type_parem)
        temp_parem_list = type_parem.split('-')
        start_date = datetime.date(int(temp_parem_list[0]), int(temp_parem_list[1]), int(temp_parem_list[2]))
        end_date = datetime.date(int(temp_parem_list[3]), int(temp_parem_list[4]), int(temp_parem_list[5]))
        article_count = Article.objects.filter(Status=1, CreateTime__range=(start_date, end_date)).count()
        content_list = Article.objects.filter(Status=1, CreateTime__range=(start_date, end_date)).order_by(
            '-CreateTime')[
                       (now_page - 1) * page_size: now_page * page_size]
    elif page_type == 'order_search_page':
        page_type_href = '%s/search/%s' % (page_type_href_head, type_parem)
        key_words = list(jieba.cut(type_parem))
        words_num = len(key_words)
        articles = None
        if words_num == 1:
            articles = Article.objects.filter(Status=1, Title__contains=key_words[0])
        elif words_num == 2:
            articles = Article.objects.filter(Status=1, Title__contains=key_words[0])\
                .filter(Title__contains=key_words[1])
        elif words_num == 3:
            articles = Article.objects.filter(Status=1, Title__contains=key_words[0])\
                .filter(Title__contains=key_words[1]).filter(Title__contains=key_words[2])
        elif words_num == 4:
            articles = Article.objects.filter(Status=1, Title__contains=key_words[0])\
                .filter(Title__contains=key_words[1]).filter(Title__contains=key_words[2])\
                .filter(Title__contains=key_words[3])
        elif words_num >= 5:
            articles = Article.objects.filter(Status=1, Title__contains=key_words[0])\
                .filter(Title__contains=key_words[1]).filter(Title__contains=key_words[2])\
                .filter(Title__contains=key_words[3]).filter(Title__contains=key_words[4])
        article_count = articles.count()
        content_list = articles.order_by('-CreateTime')[
                       (now_page - 1) * page_size: now_page * page_size]
    temp_page_count = divmod(article_count, page_size)
    if temp_page_count[1] != 0:
        page_count = temp_page_count[0] + 1
    else:
        page_count = temp_page_count[0]

    article_list = []
    for each_article in content_list:
        content = each_article.Content
        content = content.replace('#', '')
        if len(content) > 200:
            content = '%s...' % content[:200]
        article_dir = {
            'ArticleID': each_article.ArticleID,
            'DescriptionSEO': each_article.DescriptionSEO,
            'KeywordsSEO': each_article.KeywordsSEO,
            'AuthorSEO': each_article.AuthorSEO,
            'Title': each_article.Title,
            'Content': content,
            'Class': each_article.Class,
            'Label': each_article.Label,
            'PageView': each_article.PageView,
            'Status': each_article.Status,
            'TimeLine': each_article.TimeLine,
            'TimeLineType': each_article.TimeLineType,
            'CreateTime': each_article.CreateTime.strftime('%Y年%m月%d日 %H:%M:%S'),
            'UpdateTime': each_article.UpdateTime.strftime('%Y年%m月%d日 %H:%M:%S'),
        }
        class_id_list = article_dir['Class'].split(',')
        label_id_list = article_dir['Label'].split(',')
        class_name_list = get_article_class_list(class_id_list)
        label_name_list = get_article_lable_list(label_id_list)
        article_dir['class_id_list'] = class_id_list
        article_dir['class_name_list'] = class_name_list
        article_dir['label_id_list'] = label_id_list
        article_dir['label_name_list'] = label_name_list
        article_list.append(article_dir)

    if page_count <= 7:
        pages_show = [x for x in range(1, page_count + 1)]
    else:
        if now_page == 1:
            pages_show = [1, 2, 3, 4, 5, '...', page_count]
        elif now_page == 2:
            pages_show = [1, 2, 3, 4, 5, '...', page_count]
        elif now_page == 3:
            pages_show = [1, 2, 3, 4, 5, '...', page_count]
        elif now_page == 4:
            pages_show = [1, 2, 3, 4, 5, '...', page_count]
        elif page_count - now_page == 2:
            pages_show = [1, '...', now_page - 2, now_page - 1, now_page, now_page + 1, now_page + 2]
        elif page_count - now_page == 1:
            pages_show = [1, '...', now_page - 3, now_page - 2, now_page - 1, now_page, now_page + 1]
        elif page_count == now_page:
            pages_show = [1, '...', now_page - 4, now_page - 3, now_page - 2, now_page - 1, now_page]
        else:
            pages_show = [1, '...', now_page - 1, now_page, now_page + 1, '...', page_count]

    previous_page_num = now_page
    next_page_num = now_page
    if now_page != 1:
        previous_page_num = now_page - 1
    if now_page != page_count:
        next_page_num = now_page + 1

    content_dir = {
        'page_type_href': page_type_href,
        'article_list': article_list,
        'page_count': page_count,
        'pages_show': pages_show,
        'now_page': now_page,
        'previous_page_num': previous_page_num,
        'next_page_num': next_page_num,
    }
    return content_dir


def blog_class_redirect(request, class_id):
    return HttpResponseRedirect('/class/%s/1/' % class_id)


def check_cookie(func):
    def set_cookie(request, *args, **kwargs):
        cookie = request.COOKIES.get('xsz_blog_visitor')
        if not cookie:
            response = HttpResponseRedirect('/')
            response.set_cookie('xsz_blog_visitor', uuid.uuid4(), 3600 * 24 * 365 * 10)
            return response
        return func(request, *args, **kwargs)

    return set_cookie


def logger(func):
    def out_log(request, *args, **kwargs):
        log = logging.getLogger('pv')
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        visitor = request.COOKIES.get('xsz_blog_visitor')
        log.info('PV:{"PATH":"%s","VISITOR":"%s","IP":"%s"}' % (request.path, visitor, ip))
        return func(request, *args, **kwargs)

    return out_log


@check_cookie
@logger
def search(request, key_words_str, now_page):
    key_words = key_words_str.split()
    page_dir = load_sidebar()
    content_dir = load_turn_page('order_search_page', now_page, type_parem=key_words_str)
    page_dir.update(content_dir)
    page_dir.update({
        'key_words_str': key_words_str,
    })
    return render(request, 'blog/blog_search.html', page_dir)


@check_cookie
@logger
def blog_index(request):
    # img_num = random.randint(1, 10)
    # page_dir = {
    #     'img_num': img_num,
    # }
    page_dir = {
        'img_num': 10,
    }
    return render(request, 'blog/blog_index.html', page_dir)


@check_cookie
@logger
def blog_main(request, now_page):
    page_dir = load_sidebar()
    content_dir = load_turn_page('order_main_page', now_page)
    page_dir.update(content_dir)
    return render(request, 'blog/blog_main.html', page_dir)


@check_cookie
@logger
def blog_about_me(request):
    page_dir = load_sidebar()
    page_dir.update({
        'about_me_active': 'active',
    })
    return render(request, 'blog/blog_about_me.html', page_dir)


@check_cookie
@logger
def blog_time_line(request):
    page_dir = load_sidebar()
    page_dir.update({
        'time_line_active': 'active',
    })
    return render(request, 'blog/blog_time_line.html', page_dir)


@check_cookie
@logger
def blog_statistics(request):
    page_dir = load_sidebar()
    page_dir.update({
        'statistics_active': 'active',
    })
    return render(request, 'blog/blog_statistics.html', page_dir)


@check_cookie
@logger
def blog_class(request, now_class_id, now_page):
    page_dir = load_sidebar()
    content_dir = load_turn_page('order_class_page', now_page, type_parem=now_class_id)
    page_dir.update(content_dir)
    page_dir.update({
        'class_active': 'active',
        'now_class_id': int(now_class_id),
    })
    return render(request, 'blog/blog_class.html', page_dir)


@check_cookie
@logger
def blog_article_range(request, now_range, now_page):
    page_dir = load_sidebar()
    content_dir = load_turn_page('order_date_page', now_page, type_parem=now_range)
    page_dir.update(content_dir)
    page_dir.update({
        'range_active': 'active',
        'now_range': now_range,
    })
    return render(request, 'blog/blog_article_range.html', page_dir)


@check_cookie
@logger
def blog_about_my_site(request):
    page_dir = load_sidebar()
    page_dir.update({
        'about_my_site_active': 'active',
    })
    return render(request, 'blog/blog_about_my_site.html', page_dir)


@check_cookie
@logger
def blog_article(request, now_article_id):
    page_dir = load_sidebar()
    this_article = load_one_article(now_article_id)
    page_dir.update(this_article)
    for each_article in page_dir['top_article_list']:
        if this_article['this_article']['ArticleID'] == each_article['ArticleID']:
            page_dir.update({
                'top_active': 'active',
            })
    class_id_list = this_article['this_article']['Class'].split(',')
    label_id_list = this_article['this_article']['Label'].split(',')
    class_name_list = get_article_class_list(class_id_list)
    label_name_list = get_article_lable_list(label_id_list)
    page_dir.update({
        'class_id_list': class_id_list,
        'class_name_list': class_name_list,
        'label_id_list': label_id_list,
        'label_name_list': label_name_list,
    })
    return render(request, 'blog/blog_article.html', page_dir)


@staff_member_required
def change_article(request, this_article_id=None):
    page_dir = {}
    status_select = [
        {'status': 0, 'text': '不展示'},
        {'status': 1, 'text': '展示在博客上'}
    ]
    timeline_select = [
        {'status': 0, 'text': '不展示'},
        {'status': 1, 'text': '展示在时间轴上'}
    ]
    timeline_type_select = [
        {'status': 0, 'text': '默认'},
        {'status': 1, 'text': '文章'},
        {'status': 2, 'text': '图片'},
        {'status': 3, 'text': '视频'},
    ]
    classes = Class.objects.filter(Status=1)
    class_list = []
    for each_class in classes:
        class_dir = {
            'ClassID': each_class.ClassID,
            'ClassName': each_class.ClassName,
        }
        class_list.append(class_dir)
    labels = Label.objects.filter(Status=1)
    label_list = []
    for each_label in labels:
        label_dir = {
            'LabelID': each_label.LabelID,
            'LabelName': each_label.LabelName,
        }
        label_list.append(label_dir)
    page_dir.update({
        'status_select': status_select,
        'timeline_select': timeline_select,
        'timeline_type_select': timeline_type_select,
        'class_list': class_list,
        'label_list': label_list,
    })
    if this_article_id:
        this_article_id = int(this_article_id)
        this_article = load_one_article(this_article_id, 0)
        page_dir.update(this_article)
        status_selected = this_article['this_article']['Status']
        timeline_selected = this_article['this_article']['TimeLine']
        timeline_type_selected = this_article['this_article']['TimeLineType']
        page_dir.update({
            'status_selected': status_selected,
            'timeline_selected': timeline_selected,
            'timeline_type_selected': timeline_type_selected,
        })
    return render(request, 'admin/change_and_add_article.html', page_dir)


@staff_member_required
def article_save(request):
    try:
        article_data = request.POST
        this_article = None
        now_time = datetime.datetime.now()
        for temp in article_data:
            if article_data[temp]:
                if (' ' + article_data[temp]).strip() == '':
                    return HttpResponse(json.dumps({'code': '500', 'msg': '%s，为空！！！' % article_data[temp]}),
                                        content_type='application/json')
            else:
                return HttpResponse(json.dumps({'code': '500', 'msg': '参数错误！！！'}), content_type='application/json')
        if int(article_data['ArticleID']) != -1:
            this_article = Article.objects.get(ArticleID=article_data['ArticleID'])
        else:
            this_article = Article()
            this_article.CreateTime = now_time
            this_article.PageView = 0
        this_article.KeywordsSEO = article_data['KeywordsSEO']
        this_article.DescriptionSEO = article_data['DescriptionSEO']
        this_article.AuthorSEO = article_data['AuthorSEO']
        this_article.Title = article_data['Title']
        this_article.Content = article_data['Content']
        this_article.Class = article_data['Class']
        this_article.Label = article_data['Label']
        this_article.Status = article_data['Status']
        this_article.TimeLine = article_data['TimeLine']
        this_article.TimeLineType = article_data['TimeLineType']
        this_article.UpdateTime = now_time
        this_article.save()
        new_article_id = this_article.ArticleID
        return HttpResponse(json.dumps({'code': '200', 'msg': new_article_id}), content_type='application/json')
    except:
        return HttpResponse(json.dumps({'code': '500', 'msg': '写入错误！！！'}), content_type='application/json')
