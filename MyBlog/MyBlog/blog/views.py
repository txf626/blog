from django.core.paginator import Paginator
from django.shortcuts import render

from backblog.models import Article


def index(request):
    if request.method == 'GET':
        pag_id = request.GET.get('page',1)
        information = Article.objects.all()
        pa = Paginator(information,10)
        art = pa.page(pag_id)
        return render(request,'blog/index.html',{'information':art})

def share(request):
    if request.method == 'GET':
        return render(request,'blog/share.html')

def list(request):
    if request.method == 'GET':
        return render(request,'blog/list.html')

def gbook(request):
    if request.method == 'GET':
        return render(request,'blog/gbook.html')

def about(request):
    if request.method == 'GET':
        return render(request,'blog/about.html')

def info(request):
    if request.method == 'GET':
        return render(request,'blog/info.html')

def infopic(request):
    if request.method == 'GET':
        return render(request,'blog/infopic.html')


def watch(request,id):
    if request.method == 'GET':
        msg = Article.objects.filter(pk=id).first()
        return render(request,'blog/info.html',{'msg':msg})