"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from blog import views as blog_view

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/img/favicon/moying.ico')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_view.blog_index),
    url(r'^(\d+)/$', blog_view.blog_main),
    url(r'^search/(\w+)/(\d+)/$', blog_view.search),
    url(r'^about_me/$', blog_view.blog_about_me),
    url(r'^time_line/$', blog_view.blog_time_line),
    url(r'^statistics/$', blog_view.blog_statistics),
    url(r'^class/(\d+)/$', blog_view.blog_class_redirect),
    url(r'^class/(\d+)/(\d+)/$', blog_view.blog_class),
    url(r'^article_range/(\d+-\d+-\d+-\d+-\d+-\d+)/(\d+)/$', blog_view.blog_article_range),
    url(r'^about_my_site/$', blog_view.blog_about_my_site),
    url(r'^article/(\d+)/$', blog_view.blog_article),
]
