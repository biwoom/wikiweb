from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Intro_BW

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comment = forms.CharField()

# 회원 to 관리자 문의 이메일
class Contact_us_Form(forms.Form):
    name = forms.CharField(label='Your name')
    subject = forms.CharField(label='Subject')
    email = forms.EmailField(label='Your email', required=True)
    message = forms.CharField(label='Email message', widget=forms.Textarea)

# 관리자 to 회원 1인 이메일    
class Email_member_Form(forms.Form):
    mamber_name = forms.CharField(label='mamber_name')
    subject = forms.CharField(label='Subject')
    mamber_email = forms.EmailField(label='mamber_email', required=True)
    message = forms.CharField(label='Email message', widget=forms.Textarea)    

# 회원가입 커스텀 폼
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')








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