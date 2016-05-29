#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""
import json
import math
from django.db.models import Sum
from django.shortcuts import render, HttpResponse
from common.models import *
import logging

# 日志记录
logger = logging.getLogger('common.views')


# 站点基本信息
def global_setting(request):
    title = '麦子学院'
    keyword = 'IT在线教育,IT职业教育,IT培训,IT职业课程,IT职业学习,麦子学院'
    description = '麦子学院专注于IT在线职业教育,这里有超过5000+的实名学员,有硅谷IT名师参与录制的' \
                  'Android、ios、cocos2d-x开发等IT职业课程,导师在线辅导和保薪就业,更有站内IT精英实名社区,学IT就上麦子学院。'
    # 图片路径
    MEDIA_URL = settings.MEDIA_URL
    # 关键词推荐
    rcm_keyword = RecommendKeywords.objects.all()
    return locals()


# 首页
def index(request):
    # 广告信息获取
    ad_list = Ad.objects.all()
    # 教师信息
    teacher = UserProfile.objects.filter(groups__name='老师')
    # 友情链接
    links = Links.objects.all()
    # 开发者资讯
    news_reads = RecommendedReading.objects.filter(reading_type='NW').order_by('-id')
    # 官方活动
    av_reads = RecommendedReading.objects.filter(reading_type='AV').order_by('-id')
    # 技术交流
    dc_reads = RecommendedReading.objects.filter(reading_type='DC').order_by('-id')
    return render(request, "common/index.html", locals())


# 关键词ajax搜索
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
            data['course_lists'].append({'name': cl.name, 'market_page_url': cl.market_page_url, 'color': cl.course_color })
        data['career_course_lists'] = []
        for ccl in career_course_lists:
            data['career_course_lists'].append({'name': ccl.name, 'market_page_url': ccl.market_page_url, 'color': ccl.course_color})

    except Exception as e:
        logger.error(e)
    # 发送结果
    return HttpResponse(json.dumps(data), content_type="application/json")


# 首页课程ajax请求
def course_search(request):
    data = {'result': [], "error": ""}
    course_order_by = request.GET.get('course_order_by', None)
    page = int(request.GET.get("index", 1))
    try:
        if course_order_by:
            if page <= 0:
                page = 1
            if course_order_by == 'new':
                total_count = Course.objects.filter(is_homeshow=True).count()
                total_pages = math.ceil(float(total_count) / 8)
                start, end = get_start_end(page)
                result = Course.objects.filter(is_homeshow=True).order_by('-date_publish', 'id')[start:end]
                for r in result:
                    data['result'].append((r.market_page_url,  str(r.image), r.name, r.student_count))
                data['total_pages'] = int(total_pages)
                data['current_page'] = page

            elif course_order_by == 'most':
                total_count = Lesson.objects.values("course").annotate(total_play_count=Sum('play_count')).count()
                total_pages = math.ceil(float(total_count) / 8)
                start, end = get_start_end(page)
                result = Lesson.objects.values('course__market_page_url', 'course__image','course__name', 'course__student_count').annotate(total_play_count=Sum('play_count')).order_by('-total_play_count')[start:end]

                for r in result:
                    data['result'].append((r['course__market_page_url'],  r['course__image'], r['course__name'], r['course__student_count']))
                data['total_pages'] = int(total_pages)
                data['current_page'] = page

            elif course_order_by == 'hot':
                total_count = Course.objects.filter(is_homeshow=True).count()
                total_pages = math.ceil(float(total_count) / 8)
                start, end = get_start_end(page)
                result = Course.objects.filter(is_homeshow=True).order_by('-student_count', 'id')[start:end]
                for r in result:
                    data['result'].append((r.market_page_url, str(r.image), r.name, r.student_count))
                data['total_pages'] = int(total_pages)
                data['current_page'] = page
            else:
                data['error'] = '参数错误'
        else:
            data['error'] = '找不到传递的值'
    except Exception as e:
        logger.error(e)
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_start_end(page):
    start = (page - 1) * 8
    end = page * 8
    return start, end


# 老师的详细页面
def teacher_profile(request, teacher_id):
    try:
        if teacher_id:
            teacher = UserProfile.objects.get(id=teacher_id)
            course = Course.objects.filter(teacher_id=teacher_id)
    except Exception as e:
        logger.error(e)
    return render(request, 'common/teacher_profile.html', locals())



