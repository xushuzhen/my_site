# coding:utf-8
from django.db import models


# Create your models here.
class Class(models.Model):
    ClassID = models.AutoField(u'类ID', primary_key=True, max_length=11)
    ClassName = models.CharField(u'类名', max_length=20)
    ClassAbstract = models.CharField(u'类简介', max_length=50)
    Status = models.IntegerField(u'状态')
    CreateTime = models.DateTimeField(u'创建时间')
    UpdateTime = models.DateTimeField(u'更新时间')


class Lable(models.Model):
    LableID = models.AutoField(u'标签ID', primary_key=True, max_length=11)
    LableName = models.CharField(u'标签名', max_length=20)
    Status = models.IntegerField(u'状态')
    CreateTime = models.DateTimeField(u'创建时间')
    UpdateTime = models.DateTimeField(u'更新时间')


class Article(models.Model):
    ArticleID = models.AutoField(u'文章ID', primary_key=True, max_length=11)
    DescriptionSEO = models.CharField(u'SEO简介', max_length=500)
    KeywordsSEO = models.CharField(u'SEO关键字', max_length=100)
    AuthorSEO = models.CharField(u'SEO作者', max_length=20)
    Title = models.CharField(u'标题', max_length=100)
    Content = models.TextField(u'正文')
    Class = models.CharField(u'类别', max_length=20)
    Lable = models.CharField(u'标签', max_length=20)
    PageView = models.IntegerField()
    Status = models.IntegerField(u'状态')
    CreateTime = models.DateTimeField(u'创建时间')
    UpdateTime = models.DateTimeField(u'更新时间')
