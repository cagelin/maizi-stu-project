#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""
import logging
from django.shortcuts import render ,HttpResponse
from common.models import *
from django.core.serializers import serialize


# 日志记录
logger = logging.getLogger('common.views')


# 首页
def index(request):
    # 广告信息获取
    ad_list = Ad.objects.all()
    # 关键词推荐
    rcm_keyword = RecommendKeywords.objects.all()
    # 教师信息
    # teacher =
    return render(request, "common/index.html", locals())


# ajax搜索
def search(request):
    word = request.GET.get('word', None)
    try:
        if word:
            career_word = CareerCourse.objects.filter(name__icontains=word)
            career_word_list = serialize('json', career_word)
            print career_word_list
        else:
            career_word_list = None
    except Exception as e:
        logger.error(e)
    return HttpResponse(career_word_list, content_type='application/json')


