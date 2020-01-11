#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Author  : jinjianfeng
# @Contact : 553041800@qq.com
# @Link    : https://github.com/jinjf553
# @software: PyCharm
# @Date    : 2020/1/11 17:20
# @Version : ??
from django.contrib.auth import views as user_views
from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    path('login/', user_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('logout/', user_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),
]
