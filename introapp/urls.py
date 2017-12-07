from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.intro_home, name='intro_home'),
    url(r'^contact_us/$', views.email_contact_us, name='email_contact_us'),
    url(r'^email_one/$', views.email_send_one, name='email_send_one'),
    url(r'^list/$', views.intro_list, name='intro_list'),
    url(r'^(?P<pk>\d+)/$', views.intro_detail, name='intro_detail'),
    url(r'^new/$', views.intro_new, name='intro_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.intro_edit, name='intro_edit'),
]