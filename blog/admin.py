# coding:utf-8
from django.contrib import admin
from blog.models import Class
from blog.models import Lable
from blog.models import Article


# Register your models here.
def status_false(modeladmin, request, queryset):
    queryset.update(Status=0)


def status_true(modeladmin, request, queryset):
    queryset.update(Status=1)


status_true.short_description = "状态置1"
status_false.short_description = "状态置0"


@admin.register(Class)
class ClassDisplay(admin.ModelAdmin):
    list_display = ('ClassID', 'ClassName', 'ClassAbstract', 'Status', 'CreateTime', 'UpdateTime')
    search_fields = ('ClassID', 'ClassName')
    list_filter = ('Status',)
    list_per_page = 10
    actions = [status_true, status_false]


@admin.register(Lable)
class LableDisplay(admin.ModelAdmin):
    list_display = ('LableID', 'LableName', 'Status', 'CreateTime', 'UpdateTime')
    search_fields = ('LableID', 'LableName')
    list_filter = ('Status',)
    list_per_page = 10
    actions = [status_true, status_false]


@admin.register(Article)
class ArticleDisplay(admin.ModelAdmin):
    list_display = (
        'ArticleID', 'Title', 'PageView', 'Status', 'Class', 'Lable', 'CreateTime', 'UpdateTime')
    search_fields = ('ArticleID', 'Title')
    list_filter = ('Class', 'Status')
    list_per_page = 10
    actions = [status_true, status_false]


admin.site.site_header = "66哒"
