from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
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
    


# Login view
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("list_all_books")  # redirect to some page after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# Logout view
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after registration
            messages.success(request, f"Account created for {user.username}!")
            return redirect("list_all_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Create Role-Based Views

# admin_view
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "relationship_app/admin_view.html")

# librarian_view
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, "relationship_app/librarian_view.html")

# member_view
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, "relationship_app/member_view.html")



# Update views to enforce permissions

# Add book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


# Edit book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# Delete book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})