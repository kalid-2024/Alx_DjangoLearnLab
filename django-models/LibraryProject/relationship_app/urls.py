from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='list_all_books'),

    # Class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]