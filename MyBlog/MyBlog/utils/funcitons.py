"""__author__=txf"""
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backblog.models import User, Token


def is_log(foo):
    def log_required(request,*args,**kwargs):
        token = request.COOKIES.get('txf')
        user = Token.objects.filter(value=token).first()
        if not user:
            return HttpResponseRedirect(reverse('super:login'))
        return  foo(request,*args,**kwargs)
    return log_required


