from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view:
class LibraryDetailView(DetailView): 
    model = Library
    template_name = "relationship_app/library_detail.html"  # Create this template
    context_object_name = "library"

    # Add all books in the library to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context