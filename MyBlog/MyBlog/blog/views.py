from django.core.paginator import Paginator
from django.shortcuts import render

from backblog.models import Article, Banner


def index(request):
    if request.method == 'GET':
        pag_id = request.GET.get('page',1)
        information = Article.objects.all()
        pa = Paginator(information,4)
        art = pa.page(pag_id)
        ban = Banner.objects.all()
        return render(request,'blog/index.html',{'information':art,'ban':ban})

def share(request):
    if request.method == 'GET':
        return render(request,'blog/share.html')

def list(request):
    if request.method == 'GET':
        pag_id = request.GET.get('page', 1)
        information = Article.objects.all()
        pa = Paginator(information, 8)
        art = pa.page(pag_id)
        ban = Banner.objects.all()
        return render(request, 'blog/list.html', {'information': art, 'ban': ban})


def gbook(request):
    if request.method == 'GET':
        return render(request,'blog/gbook.html')

def about(request):
    if request.method == 'GET':
        return render(request,'blog/about.html')

def info(request):
    if request.method == 'GET':
        msg = Article.objects.all().first()
        return render(request,'blog/info.html',{'msg':msg})

def infopic(request):
    if request.method == 'GET':
        return render(request,'blog/infopic.html')


def watch(request,id):
    if request.method == 'GET':
        msg = Article.objects.filter(pk=id).first()
        return render(request,'blog/info.html',{'msg':msg})