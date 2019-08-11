#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Author  : jinjianfeng
# @Contact : 553041800@qq.com
# @Link    : https://github.com/jinjf553
# @software: PyCharm
# @Date    : 2019/8/10 15:05
# @Version : ??
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_title, name='blog_title'),
    path('<int:article_id>/', views.blog_article, name='blog_article'),
]
