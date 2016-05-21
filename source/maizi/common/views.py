#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""
import logging
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpRequest
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
    data = dict()
    # 获取关键词
    keyword = request.GET.get('word', None)
    try:
        # 搜索
        if keyword:
            course_lists = Course.objects.filter(name__icontains=keyword)

            career_course_lists = CareerCourse.objects.filter(name__icontains=keyword)

        else:
            course_lists = Course.objects.all()
            career_course_lists = CareerCourse.objects.all()
        # 处理
        data['course_lists'] = []
        for cl in course_lists:
            data['course_lists'].append({'name': cl.name, 'market_page_url': cl.market_page_url, 'color': cl.course_color})
        data['career_course_lists'] = []
        for ccl in career_course_lists:
            data['career_course_lists'].append({'name': ccl.name, 'market_page_url': ccl.market_page_url, 'color': ccl.course_color})
        print data
        # if course_lists:
        #     course_list = list(course_lists)
        #     data = json.dumps(course_list)
        #
        #     return HttpResponse(data)
        # else:
        #     return None
    except Exception as e:
        pass
        # logger.error(e)
    # 发送结果
    return HttpResponse(json.dumps(data), content_type="application/json")


