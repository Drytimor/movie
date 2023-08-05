from django.shortcuts import render
from .models import Book

# Create your views here.


def show_book_all(requests):
    book = Book.objects.all()
    return render(requests, 'book_app/html/book_app.html', {
        'book': book,
    })
