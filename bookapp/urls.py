from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.book_home, name='book_home'),
    url(r'^list/$', views.book_list, name='book_list'),
    url(r'^(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^new/$', views.book_new, name='book_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.book_edit, name='book_edit'),
]