from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'destroy':  
            return [IsAdminUser()]
        return [IsAuthenticated()]