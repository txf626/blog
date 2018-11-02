import time

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from backblog.form import UserForm
from backblog.models import User, Token, Article, Banner
from utils.funcitons import is_log


def login(request):
    if request.method == 'GET':
        Token.objects.filter(user_id=1).delete()
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

@is_log
def article(request):
    if request.method == 'GET':
        msg = Article.objects.filter(is_delete=0)
        return render(request,'backblog/article.html',{'msg':msg})


@is_log
def add_article(request):
    if request.method == 'GET':
        mgs = Banner.objects.all()
        return render(request,'backblog/add_article.html',{'msg':mgs})
    if request.method == 'POST':
        data = request.POST
        new_dict = {'title':data.get('title'), 'keyword': data.get('keywords'),
                    'description': data.get('describe'),
                    'label': data.get('tags'),'father_node_id':int(data.get('category')),
                    'content':data.get('content')}

        res = Article.objects.create(img=request.FILES.get('img'),**new_dict)
        if res:
            return HttpResponseRedirect(reverse('super:article'))
        return render(request,'backblog/add_article.html',{'msg':'错误'})


def update_article(request,id=None):
    if request.method =='GET':
        msg = Article.objects.filter(id=id).first()
        all = Banner.objects.all()
        return render(request,'backblog/update_article.html',{'msg':msg,'info':all})

    if request.method == 'POST':
        data = request.POST
        new_dict = {'title': data.get('title'), 'keyword': data.get('keywords'),
                    'description': data.get('describe'),
                    'label': data.get('tags'), 'father_node_id': data.get('category') ,
                    'content': data.get('content')}
        result = Article.objects.filter(id=id).update(img=request.FILES.get('img'),**new_dict)
        if result:
            return HttpResponseRedirect(reverse('super:article'))
        else:
            msg = Article.objects.filter(id=id).first()
            return render(request, 'backblog/update_article.html', {'msg': msg})

def delete(request,id):
    if request.method == 'GET':
        art = Article.objects.filter(pk=id).first()
        art.is_delete = 1
        art.save()
        return article(request)


def category(request):
    if request.method == 'GET':
        msg = Banner.objects.all()
        return render(request,'backblog/category.html',{'msg':msg})
    if request.method == 'POST':
        data = request.POST
        new_dict = {'name':data.get('name'),'name_alis':data.get('alias'),
                    'father_node':data.get('fid'),'keyword':data.get('keywords'),
                    'description':data.get('describe')}
        Banner.objects.create(**new_dict)

        msg = Banner.objects.all()
        return render(request, 'backblog/category.html', {'msg': msg})


def del_cate(request,id):
    if request.method == 'GET':
        Banner.objects.filter(pk=id).first().article_set.all().delete()
        Banner.objects.filter(pk=id).delete()
        msg = Banner.objects.all()
        return render(request, 'backblog/category.html', {'msg': msg})


def upd_cate(request,id):
    if request.method == 'GET':
        msg = Banner.objects.filter(pk=id).first()
        all_id = Banner.objects.all()
        return render(request,'backblog/update-category.html',{'msg':msg,'all':all_id})

    if request.method == 'POST':
        data = request.POST
        new_dict = {'name': data.get('name'), 'name_alis': data.get('alias'),
                    'father_node': data.get('fid'), 'keyword': data.get('keywords'),
                    'description': data.get('describe')}
        Banner.objects.filter(pk=id).update(**new_dict)

        msg = Banner.objects.all()
        return render(request, 'backblog/category.html', {'msg': msg})
