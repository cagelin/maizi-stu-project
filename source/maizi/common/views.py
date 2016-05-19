#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""
import logging
from django.shortcuts import render, HttpResponse
from common.models import *
from django.core.serializers import serialize
import json

# 日志记录
# logger = logging.getLogger('common.views')


# 首页
def index(request):
    # 广告信息获取
    ad_list = Ad.objects.all()
    # 关键词推荐
    rcm_keyword = RecommendKeywords.objects.all()
    # 教师信息
    # teacher =
    # 友情链接
    links = Links.objects.all()
    # 开发者资讯
    NEWS_reads = RecommendedReading.objects.filter(reading_type='NW')
    # 官方活动
    AV_reads = RecommendedReading.objects.filter(reading_type='AV')
    # 技术交流
    DC_reads = RecommendedReading.objects.filter(reading_type='DC')
    return render(request, "common/index.html", locals())


# ajax搜索
def keyword_search(request):
    # 获取关键词
    keyword = request.GET.get('word', None)
    try:
        # 搜索
        out =[]
        career_course_list = CareerCourse.objects.filter(name__icontains=keyword).values('id','name')
        course_list = Course.objects.filter(name__icontains=keyword).values('id','name')
        for ccl in career_course_list:
            out.append(ccl)
        for cl in course_list:
            out.append(cl)
        print out
        # 处理结果
    except Exception as e:
        pass
        # logger.error(e)
    # 发送结果
    return HttpResponse(out)


