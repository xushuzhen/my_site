# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_timelinetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='TimeLineType',
            field=models.IntegerField(verbose_name='\u65f6\u95f4\u8f74\u7c7b\u578b'),
        ),
    ]
