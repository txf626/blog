"""__author__=txf"""
from django.conf.urls import url

from backblog import views

urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^index/',views.index,name='index'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^article/',views.article,name='article'),
    url(r'^add_article/',views.add_article,name='add_article')
]