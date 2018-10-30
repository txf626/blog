from django.shortcuts import render

def index(request):
    if request.method == 'GET':
        return render(request,'blog/index.html')

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