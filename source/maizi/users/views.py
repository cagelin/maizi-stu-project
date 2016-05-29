# coding:utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from users.form import *
# Create your views here.


# 登入
def do_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)
            else:
                pass
            return redirect('/')
        else:
            pass


# 退出
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return redirect(request.META['HTTP_REFERER'])


