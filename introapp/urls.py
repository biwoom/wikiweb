from django.conf.urls import include, url
from . import views
from .forms import MyPasswordResetForm
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete, password_change, password_change_done
)

urlpatterns = [
    # 홈
    url(r'^$', views.inb_home, name='inb_home'),
    # 이메일
    url(r'^contact_us/$', views.email_contact_us, name='email_contact_us'),
    url(r'^email_one/$', views.email_send_one, name='email_send_one'),
    url(r'^email_all/$', views.email_send_all, name='email_send_all'),
    # 로그인 / # 로그아웃
    url(r'^login/$', login, {'template_name': 'introapp/account/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'introapp/account/logout.html'}, name='logout'),
    # 비밀번호 변경
    url(r'^password_change/$', password_change, {
        'template_name': 'introapp/account/password_change_form.html'}, name='password_change'),
    url(r'^password_change/done/$', password_change_done, {
        'template_name': 'introapp/account/password_change_done.html'}, name='password_change_done'),    
    # 회원가입
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # 비밀번호 리셋
    url(r'^reset-password/$', password_reset, {
        'password_reset_form':MyPasswordResetForm,
        'template_name': 'introapp/account/reset_password.html', 
        'email_template_name': 'introapp/email/reset_password_email_2.html'}, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {
        'template_name': 'introapp/account/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {
        'template_name': 'introapp/account/reset_password_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{
        'template_name': 'introapp/account/reset_password_complete.html'}, name='password_reset_complete'),
        
    # 인트로
    url(r'^intro/$', views.intro_home, name='intro_home'),
    url(r'^list/$', views.intro_list, name='intro_list'),
    url(r'^(?P<pk>\d+)/$', views.intro_detail, name='intro_detail'),
    url(r'^new/$', views.intro_new, name='intro_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.intro_edit, name='intro_edit'),
]