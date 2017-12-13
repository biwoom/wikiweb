from django.conf.urls import include, url
from . import views

urlpatterns = [
    # 홈
    url(r'^$', views.inb_home, name='inb_home'),
    # 이메일
    url(r'^contact_us/$', views.email_contact_us, name='email_contact_us'),
    url(r'^email_one/$', views.email_send_one, name='email_send_one'),
    # 회원가입
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # 인트로
    url(r'^intro/$', views.intro_home, name='intro_home'),
    url(r'^list/$', views.intro_list, name='intro_list'),
    url(r'^(?P<pk>\d+)/$', views.intro_detail, name='intro_detail'),
    url(r'^new/$', views.intro_new, name='intro_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.intro_edit, name='intro_edit'),
]