from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publication_BW
from .forms import Publication_BW_Form
from django.shortcuts import redirect
# paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 검색
from django.db.models import Q


# def book_home(request):
#     return render(request, 'bookapp/book_home.html')


def book_list(request):
    # books = Publication_BW.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    books_list = Publication_BW.objects.all()
    #검색
    error_text = 0
    query = request.GET.get('q')
    if query:
        books_list = books_list.filter(
				Q(main_title__icontains=query)|
				Q(main_author__icontains=query)
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
    a_book = get_object_or_404(Publication_BW, pk=pk)
    return render(request, 'bookapp/book_detail.html', {'book': a_book})


def book_edit(request, pk):
    a_book = get_object_or_404(Publication_BW, pk=pk)
    if request.method == "POST":
        form = Publication_BW_Form(request.POST, request.FILES or None, instance=a_book)
        if form.is_valid():
            a_book = form.save(commit=False)
            # a_book.author = request.user
            a_book.re_draft_date = timezone.now()
            a_book.save()
            return redirect('book_detail', pk=a_book.pk)
    else:
        form = Publication_BW_Form(instance=a_book)
    return render(request, 'bookapp/book_edit.html', {'form': form})
            
def book_new(request):
    if not request.user.is_staff:
            return redirect('book_list') 
    else:        
        if request.method == "POST":
            form = Publication_BW_Form(request.POST, request.FILES or None)
            if form.is_valid():
                a_book = form.save(commit=False)
                # a_book.author = request.user
                a_book.re_draft_date = timezone.now()
                a_book.save()
                return redirect('book_detail', pk=a_book.pk)
        else:
            form = Publication_BW_Form()
        return render(request, 'bookapp/book_edit.html', {'form': form})
