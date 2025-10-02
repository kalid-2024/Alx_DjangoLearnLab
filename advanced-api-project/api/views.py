from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions, filters

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

        # Extra customization: automatically assign author if not provided
    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

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
