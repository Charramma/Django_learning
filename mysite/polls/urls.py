#!/bin/env python3
# -*- coding utf-8 -*-
# @Author: Charramma(Huang)
# @E-mail: huang.zyn@qq.com
# @Time: 2020/12/8 21:04
# @File: urls.py.py
# @Software: Pycharm

from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path("", views.index, name="index"),
    # /polls/5/
    path("<int:question_id>/", views.detail, name='detail'),
    # /polls/5/results/
    path("<int:question_id>/results/", views.results, name='results'),
    # /polls/5/vote/
    path("<int:quesiton_id>/vote/", views.vote, name="vote"),
]