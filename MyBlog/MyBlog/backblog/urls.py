"""__author__=txf"""
from django.conf.urls import url

from backblog import views

urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^index/',views.index,name='index'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^article/',views.article,name='article'),
    url(r'^add_article/',views.add_article,name='add_article'),
    url(r'^update_article/(\d+)',views.update_article,name='update_article'),
    url(r'^delete/(\d+)',views.delete,name='delete'),
    url(r'^category/',views.category,name='category'),
    url(r'^del_cate/(\d+)',views.del_cate,name='del_cate'),
    url(r'upd_cate/(\d+)',views.upd_cate,name='upd_cate')
]