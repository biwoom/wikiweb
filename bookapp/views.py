from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book_BW
from .forms import Book_BWForm
from django.shortcuts import redirect
# paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 검색
from django.db.models import Q
    
def book_home(request):
    return render(request, 'bookapp/book_home.html')

def book_list(request):
    # books = Book_BW.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    books_list = Book_BW.objects.all()
    #검색
    error_text = 0
    query = request.GET.get('q')
    if query:
        books_list = books_list.filter(
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
    if not books_list:
            error_text = 1
    # paginator
    paginator = Paginator(books_list, 20) # Show 25 books per page
    page = request.GET.get('page')
    try:
        bookset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bookset = paginator.page(1)
        # error_text = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bookset = paginator.page(paginator.num_pages)
    if error_text == 0:
        return render(request, 'bookapp/book_list.html', {'books': bookset})
    else: 
        return render(request, 'bookapp/book_list.html', {'books': bookset, 'error_text':error_text})


def book_detail(request, pk):
    a_book = get_object_or_404(Book_BW, pk=pk)
    return render(request, 'bookapp/book_detail.html', {'book': a_book})


def book_edit(request, pk):
    a_book = get_object_or_404(Book_BW, pk=pk)
    if request.method == "POST":
        form = Book_BWForm(request.POST, request.FILES or None, instance=a_book)
        if form.is_valid():
            a_book = form.save(commit=False)
            a_book.author = request.user
            a_book.published_date = timezone.now()
            a_book.save()
            return redirect('book_detail', pk=a_book.pk)
    else:
        form = Book_BWForm(instance=a_book)
    return render(request, 'bookapp/book_edit.html', {'form': form})
    
            
def book_new(request):
    if not request.user.is_staff:
            return redirect('book_list') 
    else:        
        if request.method == "POST":
            form = Book_BWForm(request.POST, request.FILES or None)
            if form.is_valid():
                a_book = form.save(commit=False)
                a_book.author = request.user
                a_book.published_date = timezone.now()
                a_book.save()
                return redirect('book_detail', pk=a_book.pk)
        else:
            form = Book_BWForm()
        return render(request, 'bookapp/book_edit.html', {'form': form})
        
