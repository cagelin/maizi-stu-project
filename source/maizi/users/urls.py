#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
users模块的url配置。
"""

from django.conf.urls import patterns, url
from users.views import *
urlpatterns = patterns('users.views',
                       url(r'^login$', do_login, name='login'),
                       url(r'^logout$', do_logout, name='logout')
                       )
