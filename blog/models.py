from django.db import models


# Create your models here.
class Class(models.Model):
    ClassID = models.AutoField(primary_key=True, max_length=11)
    ClassName = models.CharField(max_length=20)
    ClassAbstract = models.CharField(max_length=50)
    Status = models.IntegerField()
    CreateTime = models.DateTimeField()
    UpdateTime = models.DateTimeField()


class Lable(models.Model):
    LableID = models.AutoField(primary_key=True, max_length=11)
    LableName = models.CharField(max_length=20)
    Status = models.IntegerField()
    CreateTime = models.DateTimeField()
    UpdateTime = models.DateTimeField()


class Article(models.Model):
    ArticleID = models.AutoField(primary_key=True, max_length=11)
    DescriptionSEO = models.CharField(max_length=500)
    KeywordsSEO = models.CharField(max_length=100)
    AuthorSEO = models.CharField(max_length=20)
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Class = models.IntegerField()
    Lable = models.IntegerField()
    PageView = models.IntegerField()
    Status = models.IntegerField()
    CreateTime = models.DateTimeField()
    UpdateTime = models.DateTimeField()
