import time

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backblog.form import UserForm
from backblog.models import User, Token
from utils.funcitons import is_log


def login(request):
    if request.method == 'GET':
        return render(request,'backblog/login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserForm(data)

        if form.is_valid():
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('userpwd')
            user = check_password(password,User.objects.filter(name=name).first().new_password)
            if user:
                ids = User.objects.filter(name=name).first().id
                value = make_password(password+str(time.time()))
                Token.objects.create(user_id=ids,key='txf',value=value)
                res = HttpResponseRedirect(reverse('super:index'))
                res.set_cookie(key='txf',value=value,max_age=1000)
                return res
            else:
                return render(request,'backblog/login.html',{'errors':'密码错误'})
        else:
            errors = form.errors
            return render(request, 'backblog/login.html', {'errors': errors})
@is_log
def index(request):
    if request.method == 'GET':
        return render(request,'backblog/index.html')

def logout(request):
    if request.method == 'GET':
        token = request.COOKIES.get('txf')
        Token.objects.filter(value=token).delete()
        res = HttpResponseRedirect(reverse('super:login'))
        res.delete_cookie('txf')
        return res


def article(request):
    if request.method == 'GET':
        return render(request,'backblog/article.html')


def add_article(request):
    if request.method == 'GET':
        return render(request,'backblog/add_article.html')