import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Library

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.filter(name=author_name)
        books = author.books.all()   # thanks to related_name
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")

# 2️⃣ List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Many-to-Many
        print(f"\nBooks in {library.name}:")
        for book in books:
            print(f"- {book.title} (Author: {book.author.name})")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

# 3️⃣ Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # One-to-One
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Exception:
        print(f"No librarian assigned for {library_name}")

if __name__ == "__main__":
    # Sample queries
    books_by_author("George Orwell")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
