from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

# Create your views here.

# Function-Based View
def list_all_books(request):
    books = Book.objects.all()
    lines = [f"{book.title} by {book.author.name}" for book in books]
    # Join lines into a simple text response
    return HttpResponse("<br>".join(lines))