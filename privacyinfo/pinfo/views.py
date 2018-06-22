from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.http import request
from pinfo import models


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = models.UserModel.objects.filter(username=username)
        eml = models.UserModel.objects.filter(email=email)
        if user:
            return render(request, 'registererr.html', {'errinfo': '用户名已经存在'})
        elif eml:
            return render(request, 'registererr.html', {'errinfo': '邮箱已被注册'})
        else:
            newuser = models.UserModel.objects.create(
                username=username, phone=phone, password=make_password(password), email=email)
            newuser.save()
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        logininfo = request.POST.get('logininfo')
        password = request.POST.get('password')
        try:
            linfo = models.UserModel.objects.get(username=logininfo)
            pwd = linfo.password
            if check_password(password, pwd):
                return HttpResponse('OK')
        except Exception:
            try:
                linfo = models.UserModel.objects.get(email=logininfo)
                pwd = linfo.password
                if check_password(password, pwd):
                    return HttpResponse('OK')
            except Exception:
                return render(request, "loginerr.html")

    return render(request, "login.html")
