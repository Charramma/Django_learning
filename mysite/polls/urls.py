#!/bin/env python3
# -*- coding utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Time: 2020/12/8 21:04
# @File: urls.py.py
# @Software: Pycharm

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    path("", views.index, name="index"),
    # /polls/1/
    path("<int:question_id>/", views.detail, name='detail'),
    # # /polls/1/results/
    # path("<int:question_id>/results/", views.results, name='results'),
    # /polls/1/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]