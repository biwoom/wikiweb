from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.blog_home, name='blog_home'),
    url(r'^list/$', views.blog_list, name='blog_list'),
    url(r'^(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^new/$', views.blog_new, name='blog_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.blog_edit, name='blog_edit'),
]