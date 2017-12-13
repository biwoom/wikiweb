from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Intro_BW
from .forms import Intro_BWForm, Contact_us_Form, Email_member_Form
from django.shortcuts import redirect
# paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 검색
from django.db.models import Q
# email
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .python_email.email_bw import EmailSender

# 홈
def inb_home(request):
    return render(request, 'introapp/home/base_home.html')

# 인트로 홈    
def intro_home(request):
    return render(request, 'introapp/intro/intro_home.html')    
    
# 이메일-문의상항   
def email_contact_us(request):
    if request.method == "POST":
        form = Contact_us_Form(request.POST, request.FILES or None)
        if form.is_valid():
            to_member_email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            member_name = form.cleaned_data.get("name")
            subject = form.cleaned_data.get("subject")
            
            try:
                send = EmailSender(to_member_email, message, member_name, subject)
                # send.sending_one()
                send.contact_us()
            except IOError:
                return HttpResponse('이메일 보내기: 실패')
            return HttpResponse('이메일 보내기: 성공')
    else:
        form = Contact_us_Form()
    return render(request, 'introapp/email/email_contact_us.html', {'form': form})    

# 이메일-개인맴버
def email_send_one(request):
    if request.method == "POST":
        form = Email_member_Form(request.POST, request.FILES or None)
        if form.is_valid():
            to_member_email = form.cleaned_data.get("mamber_email")
            message = form.cleaned_data.get("message")
            member_name = form.cleaned_data.get("mamber_name")
            subject = form.cleaned_data.get("subject")
            
            try:
                send = EmailSender(to_member_email, message, member_name, subject)
                send.sending_one()
            except IOError:
                return HttpResponse('이메일 보내기: 실패')
            return HttpResponse('이메일 보내기: 성공')
    else:
        form = Email_member_Form()
    return render(request, 'introapp/email/email_send_one.html', {'form': form})  






def intro_list(request):
    # intros = Intro_BW.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    intros_list = Intro_BW.objects.all()
    #검색
    error_text = 0
    query = request.GET.get('q')
    if query:
        intros_list = intros_list.filter(
				Q(title__icontains=query)|
				Q(text__icontains=query) |
				Q(ti_wylie__icontains=query)|
				Q(ti_past_tense__icontains=query)|
				Q(ti_present_tense__icontains=query)|
				Q(ti_future_tense__icontains=query)|
				Q(ti_imperative__icontains=query)|
				Q(ti_synonym__icontains=query)|
				Q(ti_thesaurus__icontains=query)|
				Q(ti_antonym__icontains=query)|
				Q(ti_honorific__icontains=query)|
				Q(ti_humble_terms__icontains=query)|
				Q(ti_korean_entry__icontains=query)|
				Q(ti_sanskrit_entry__icontains=query)|
				Q(ti_pali_entry__icontains=query)|
				Q(ti_classical_chinese_entry__icontains=query)|
				Q(ti_english_entry__icontains=query)
				).distinct()
    if not intros_list:
            error_text = 1
    # paginator
    paginator = Paginator(intros_list, 20) # Show 25 intros per page
    page = request.GET.get('page')
    try:
        introset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        introset = paginator.page(1)
        # error_text = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        introset = paginator.page(paginator.num_pages)
    if error_text == 0:
        return render(request, 'introapp/intro/intro_list.html', {'intros': introset})
    else: 
        return render(request, 'introapp/intro/intro_list.html', {'intros': introset, 'error_text':error_text})


def intro_detail(request, pk):
    a_intro = get_object_or_404(Intro_BW, pk=pk)
    return render(request, 'introapp/intro/intro_detail.html', {'intro': a_intro})


def intro_edit(request, pk):
    a_intro = get_object_or_404(Intro_BW, pk=pk)
    if request.method == "POST":
        form = Intro_BWForm(request.POST, request.FILES or None, instance=a_intro)
        if form.is_valid():
            a_intro = form.save(commit=False)
            a_intro.author = request.user
            a_intro.published_date = timezone.now()
            a_intro.save()
            return redirect('intro_detail', pk=a_intro.pk)
    else:
        form = Intro_BWForm(instance=a_intro)
    return render(request, 'introapp/intro/intro_edit.html', {'form': form})
    
            
def intro_new(request):
    if not request.user.is_staff:
            return redirect('intro_list') 
    else:        
        if request.method == "POST":
            form = Intro_BWForm(request.POST, request.FILES or None)
            if form.is_valid():
                a_intro = form.save(commit=False)
                a_intro.author = request.user
                a_intro.published_date = timezone.now()
                a_intro.save()
                return redirect('intro_detail', pk=a_intro.pk)
        else:
            form = Intro_BWForm()
        return render(request, 'introapp/intro/intro_edit.html', {'form': form})
        
# def intro_new(request):
#     form = Intro_BWForm()
#     return render(request, 'introapp/intro_edit.html', {'form': form})