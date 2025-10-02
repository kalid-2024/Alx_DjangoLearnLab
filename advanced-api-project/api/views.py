from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
     # Filtering options
    filterset_fields = ['title', 'author', 'publication_year']
    # Search options
    search_fields = ['title', 'publication_year']
    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

        # Extra customization: automatically assign author if not provided
    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



# Book Views:
# - ListView: Retrieve all books (public)
# - DetailView: Retrieve single book by ID (public)
# - CreateView: Add new book (authenticated only)
# - UpdateView: Modify book (authenticated only)
# - DeleteView: Remove book (authenticated only)
#
# Permissions:
# - AllowAny for safe methods (list, retrieve)
# - IsAuthenticated for create/update/delete


# BookListView supports:
# - Filtering: /api/books/?title=1984&author=1&publication_year=1949
# - Searching: /api/books/?search=keyword (searches title and author name)
# - Ordering: /api/books/?ordering=title or ?ordering=-publication_year (descending order or newest first)
#
# Example: /api/books/?search=Orwell&ordering=-publication_year
# → returns Orwell's books ordered by newest first