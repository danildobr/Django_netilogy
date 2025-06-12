from django.shortcuts import render
from .models import Book
from django.db.models import Q

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)

def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    books = Book.objects.filter(pub_date=pub_date)
    
    # Получаем предыдущую и следующую даты
    prev_date = Book.objects.filter(
        pub_date__lt=pub_date
    ).order_by('-pub_date').values('pub_date').first()
    
    next_date = Book.objects.filter(
        pub_date__gt=pub_date
    ).order_by('pub_date').values('pub_date').first()
    
    context = {
        'books': books,
        'prev_date': prev_date['pub_date'] if prev_date else None,
        'next_date': next_date['pub_date'] if next_date else None,
        'current_date': pub_date,
    }
    return render(request, template, context)