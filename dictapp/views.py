from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Dict
from .forms import DictForm
from django.shortcuts import redirect
# paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 검색
from django.db.models import Q

def dict_home(request):
    return render(request, 'dictapp/dict_home.html')

def dict_list(request):
    # dicts = Dict.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    dicts_list = Dict.objects.all()
    #검색
    error_text = 0
    query = request.GET.get('q')
    if query:
        dicts_list = dicts_list.filter(
				Q(title__icontains=query)|
				Q(text__icontains=query)
				).distinct()
    if not dicts_list:
            error_text = 1
    # paginator
    paginator = Paginator(dicts_list, 20) # Show 25 dicts per page
    page = request.GET.get('page')
    try:
        dictset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dictset = paginator.page(1)
        # error_text = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dictset = paginator.page(paginator.num_pages)
    if error_text == 0:
        return render(request, 'dictapp/dict_list.html', {'dicts': dictset})
    else: 
        return render(request, 'dictapp/dict_list.html', {'dicts': dictset, 'error_text':error_text})


def dict_detail(request, pk):
    a_dict = get_object_or_404(Dict, pk=pk)
    return render(request, 'dictapp/dict_detail.html', {'dict': a_dict})


def dict_edit(request, pk):
    a_dict = get_object_or_404(Dict, pk=pk)
    if request.method == "POST":
        form = DictForm(request.POST, request.FILES or None, instance=a_dict)
        if form.is_valid():
            a_dict = form.save(commit=False)
            a_dict.author = request.user
            a_dict.published_date = timezone.now()
            a_dict.save()
            return redirect('dict_detail', pk=a_dict.pk)
    else:
        form = DictForm(instance=a_dict)
    return render(request, 'dictapp/dict_edit.html', {'form': form})
    
            
def dict_new(request):
    if not request.user.is_staff:
            return redirect('dict_list') 
    else:        
        if request.method == "POST":
            form = DictForm(request.POST, request.FILES or None)
            if form.is_valid():
                a_dict = form.save(commit=False)
                a_dict.author = request.user
                a_dict.published_date = timezone.now()
                a_dict.save()
                return redirect('dict_detail', pk=a_dict.pk)
        else:
            form = DictForm()
        return render(request, 'dictapp/dict_edit.html', {'form': form})
        
