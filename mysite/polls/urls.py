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
    path("", views.IndexView.as_view(), name="index"),
    # /polls/1/
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    # /polls/1/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name='results'),
    # /polls/1/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
