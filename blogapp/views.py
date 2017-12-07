from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Blog_BW
from .forms import Blog_BWForm
from django.shortcuts import redirect
# paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 검색
from django.db.models import Q
  
def blog_home(request):
    return render(request, 'blogapp/blog_home.html')

def blog_list(request):
    # blogs = Blog_BW.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    blogs_list = Blog_BW.objects.all()
    #검색
    error_text = 0
    query = request.GET.get('q')
    if query:
        blogs_list = blogs_list.filter(
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
    if not blogs_list:
            error_text = 1
    # paginator
    paginator = Paginator(blogs_list, 20) # Show 25 blogs per page
    page = request.GET.get('page')
    try:
        blogset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogset = paginator.page(1)
        # error_text = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogset = paginator.page(paginator.num_pages)
    if error_text == 0:
        return render(request, 'blogapp/blog_list.html', {'blogs': blogset})
    else: 
        return render(request, 'blogapp/blog_list.html', {'blogs': blogset, 'error_text':error_text})


def blog_detail(request, pk):
    a_blog = get_object_or_404(Blog_BW, pk=pk)
    return render(request, 'blogapp/blog_detail.html', {'blog': a_blog})


def blog_edit(request, pk):
    a_blog = get_object_or_404(Blog_BW, pk=pk)
    if request.method == "POST":
        form = Blog_BWForm(request.POST, request.FILES or None, instance=a_blog)
        if form.is_valid():
            a_blog = form.save(commit=False)
            a_blog.author = request.user
            a_blog.published_date = timezone.now()
            a_blog.save()
            return redirect('blog_detail', pk=a_blog.pk)
    else:
        form = Blog_BWForm(instance=a_blog)
    return render(request, 'blogapp/blog_edit.html', {'form': form})
    
            
def blog_new(request):
    if not request.user.is_staff:
            return redirect('blog_list') 
    else:        
        if request.method == "POST":
            form = Blog_BWForm(request.POST, request.FILES or None)
            if form.is_valid():
                a_blog = form.save(commit=False)
                a_blog.author = request.user
                a_blog.published_date = timezone.now()
                a_blog.save()
                return redirect('blog_detail', pk=a_blog.pk)
        else:
            form = Blog_BWForm()
        return render(request, 'blogapp/blog_edit.html', {'form': form})
        
