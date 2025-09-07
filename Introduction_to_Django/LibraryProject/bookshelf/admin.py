from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters on the right sidebar
    list_filter = ("author", "publication_year")

    # Add a search box
    search_fields = ("title", "author") 