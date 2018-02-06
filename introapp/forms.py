from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Intro_BW

from custom_utils.email.python_email import EmailSender
from custom_utils.basic_info import SERVER_DOMAIN, EMAIL_HOST_NAME

from django.template import loader
import unicodedata
from django import forms
from django.contrib.auth import (authenticate, get_user_model, password_validation,)
from django.contrib.auth.hashers import (UNUSABLE_PASSWORD_PREFIX, identify_hasher,)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.validators import RegexValidator



class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comment = forms.CharField()

# 일시후원 이메일
class One_time_donation_Form(forms.Form):
    username = forms.CharField(label='아이디', required=False)
    name = forms.CharField(label='성명', help_text='성명과 입금자명은 일치해야 합니다.', required=True)
    birth = forms.IntegerField(label='생년월일', help_text='숫자만 입력하세요. 예)19870610', required=True)
    mobile = forms.IntegerField(label='휴대전화', help_text='숫자만 입력하세요. 예)01012345678', required=True)
    email = forms.EmailField(label='이메일', required=True)
    addess = forms.CharField(label='주소', required=True)
    amount_of_donation = forms.IntegerField(label='후원금액', required=True)
    donation_message = forms.CharField(label='의견사항', widget=forms.Textarea(attrs={'height':200, 'cols' : 10, 'rows': 5 }), required=False)
    use_agreement = forms.BooleanField(label='이용약관', help_text='이용약관에 동의합니다.')
    privacy_policy_statement = forms.BooleanField(label='개인정보취급방침')

# 회원 to 관리자 문의 이메일
class Contact_us_Form(forms.Form):
    name = forms.CharField(label='이름')
    subject = forms.CharField(label='주제')
    email = forms.EmailField(label='이메일', required=True)
    message = forms.CharField(label='이메일 내용', widget=forms.Textarea)
    
# 관리자 to 전체회원 이메일    
class Email_all_member_Form(forms.Form):
    subject = forms.CharField(label='주제')
    message = forms.CharField(label='이메일 내용', widget=forms.Textarea)    

# 관리자 to 회원 1인 이메일    
class Email_member_Form(forms.Form):
    mamber_name = forms.CharField(label='mamber_name')
    subject = forms.CharField(label='Subject')
    mamber_email = forms.EmailField(label='mamber_email', required=True)
    message = forms.CharField(label='Email message', widget=forms.Textarea)  
    
# 회원가입 커스텀 폼
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', label='이메일')
    
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', '오직 알파벳만 사용할 수 있습니다.')

    username = forms.CharField(max_length=200, validators=[alphanumeric],  label='아이디')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email 주소가 이미 존재합니다')
        return email
        
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# 비밀번호 변경 폼 커스텀
class MyPasswordResetForm(PasswordResetForm):
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        
        # 커스텀 이메일 모듈 연결
        email_message = EmailSender(to_email, body, to_email, subject)
        
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        # email_message.sending_one()
        email_message.sending_one()
        # email_message.sending_with_img()
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Email 주소가 존재하지 않습니다.')
        return email
        
    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
            
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'email': user.email,
                'domain': SERVER_DOMAIN,
                'site_name': EMAIL_HOST_NAME,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            if extra_email_context is not None:
                context.update(extra_email_context)
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                user.email, html_email_template_name=html_email_template_name,
            )

# 로그인 폼 커스텀
class MyAuthenticationForm(AuthenticationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Email 주소가 존재하지 않습니다.')
        return email
        
    def clean_username(self):    
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'아이디가 존재하지 않습니다.')
        return username
        
 
# username 찾기 폼
class FindUsernameForm(forms.Form):
    email = forms.EmailField(label='이메일', required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Email 주소가 존재하지 않습니다.')
        return email
            
        
    
# ===============================================
# ===============================================
# ===============================================

class Intro_BWForm(forms.ModelForm):
    class Meta:
        model = Intro_BW
        fields = (
            # 티벳어 표제어
            'title',
            # 티벳어-와일리 필드
            'ti_wylie',
            # 티벳어 한글 설명
            'text',
            # 티벳어 동사 과거형 필드
            'ti_past_tense',
            # 티벳어 동사 현재형 필드
            'ti_present_tense',
            # 티벳어 동사 미래형 필드
            'ti_future_tense',
            # 티벳어 동사 명령형 필드
            'ti_imperative',
            # 티벳어 유의어 필드
            'ti_thesaurus',
            # 티벳어 반의어 필드
            'ti_antonym',
            # 티벳어 높임말 필드
            'ti_honorific',
            # 티벳어 낮춤말 필드
            'ti_humble_terms',
            # 한국어 표제어 필드
            'ti_korean_entry',
            # 범어 표제어 필드
            'ti_sanskrit_entry',
            # 빨리어 표제어 필드
            'ti_pali_entry',
            # 한문 표제어 필드
            'ti_classical_chinese_entry',
            # 영어 표제어 필드
            'ti_english_entry',
            # 티벳어 이미지
            'image', 
            # 티벳어 발음 오디오
            'audio',
            )            