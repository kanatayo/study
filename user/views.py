from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views import View

from video.models import Video
from .models import CustomerUser


# Create your views here.


class login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        userName = request.POST.get('userName')
        userPassword = request.POST.get('password')
        db_user = CustomerUser.objects.filter(username=userName).first()
        if db_user:
            print(db_user)
            if db_user.check_password(userPassword):
                auth_login(request, db_user)
                return redirect('/video/index/')
            else:
                return render(request, 'login.html', {'error': '密码错误'})
        else:
            return render(request, 'login.html', {'error': '账号不存在'})


def logout(request):
    auth_logout(request)
    return redirect('/video/list/')


class register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        userName = request.POST.get('userName')
        userPassword = request.POST.get('password')
        passwordAgain = request.POST.get('passwordAgain')
        db_user = CustomerUser.objects.filter(username=userName).first()
        if db_user:
            return render(request, 'register.html', {'error': '用户名已存在'})
        else:
            if passwordAgain != userPassword:
                return render(request, 'register.html', {'error': '两次输入的密码不相同'})
            else:
                CustomerUser.objects.create_user(username=userName, password=userPassword)
                return redirect('/user/login/')


def my(request):
    videos = request.user.video.all()
    return render(request, 'my.html', {"videos": videos})
