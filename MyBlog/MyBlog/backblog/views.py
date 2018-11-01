import time

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from backblog.form import UserForm
from backblog.models import User, Token, Article
from utils.funcitons import is_log


def login(request):
    if request.method == 'GET':
        token = request.COOKIES.get('txf')
        Token.objects.filter(value=token).delete()
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
        msg = Article.objects.all()
        return render(request,'backblog/article.html',{'msg':msg})


def add_article(request):
    if request.method == 'GET':
        return render(request,'backblog/add_article.html')
    if request.method == 'POST':
        data = request.POST
        new_dict = {'title':data.get('title'), 'keyword': data.get('keywords'),
                    'description': data.get('describe'),
                    'label': data.get('tags'),'father_node_id':data.get('category'),
                    'img':data.get('titlepic'),'content':data.get('content')}

        res = Article.objects.create(**new_dict)
        if res:
            return HttpResponse('OK')
        return render(request,'backblog/add_article.html',{'msg':'错误'})

def update_article(request,id):
    if request.method =='GET':
        msg = Article.objects.filter(id=id).first()
        return render(request,'backblog/update_article.html',{'msg':msg})
