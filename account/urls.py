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
    path('password-change/', user_views.PasswordChangeView.as_view(template_name="account/password_change_form.html",
                                                                   success_url="/account/password-changed-done/"),
         name='password_change'),
    path('password-changed-done/', user_views.PasswordChangeDoneView.as_view(
        template_name='account/password_changed_done.html'), name='password_changed_done'),
    path('password-reset/', user_views.PasswordResetView.as_view(template_name='account/password_reset_form.html',
                                                                 email_template_name='account/password_reset_email.html',
                                                                 success_url='/account/password-reset-done/'),
         name='password_reset'),
    path('password-reset-done/', user_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', user_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html', success_url='/account/password-reset-complete/'
    ), name='password_reset_confirm'),
    path('password-reset-complete/', user_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'
    ), name='password_reset_complete'),
]
