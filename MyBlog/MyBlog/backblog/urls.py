"""__author__=txf"""
from django.conf.urls import url

from backblog import views

urlpatterns = [
    url(r'login/',views.login,name='login'),
    url(r'index/',views.index,name='index')
]