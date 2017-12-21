from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.dict_home, name='dict_home'),
    url(r'^thl-dict', views.dict_thl_dictionary, name='dict_thl_dictionary'),
    url(r'^list/$', views.dict_list, name='dict_list'),
    url(r'^(?P<pk>\d+)/$', views.dict_detail, name='dict_detail'),
    url(r'^new/$', views.dict_new, name='dict_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.dict_edit, name='dict_edit'),
]


