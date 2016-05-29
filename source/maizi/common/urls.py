#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from views import *
urlpatterns = patterns('common.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^keyword_search/$', keyword_search, name='keyword_search'),
                       url(r'^course_search/$', course_search, name='course_search'),
                       url(r'^teacher/(?P<teacher_id>\d+)$', teacher_profile, name='teacher'),
)
