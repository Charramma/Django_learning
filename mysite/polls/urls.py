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
    path("", views.index, name='index'),
]