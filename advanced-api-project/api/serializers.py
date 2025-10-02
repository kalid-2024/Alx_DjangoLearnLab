from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        # Custom validation: publication_year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# AuthorSerializer:
class AuthorSerializer(serializers.ModelSerializer):
    # - Includes the author's name
    # - Uses a nested BookSerializer to represent all related books dynamically
    books = BookSerializer(many=True, read_only=True)   
    # - read_only=True ensures books are only displayed, not created via AuthorSerializer directly
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
