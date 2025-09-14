from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
     return HttpResponse("Welcome to my book store.")


# View books (requires can_view)
@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})

# Create book (requires can_create)
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form})

# Edit book (requires can_edit)
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/book_form.html", {"form": form})

# Delete book (requires can_delete)
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")

def search_books(request):
    query = request.GET.get("q", "")
    # Safe query using ORM
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})