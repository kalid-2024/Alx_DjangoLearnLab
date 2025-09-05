from bookshelf.models import Book

# Creating a Book instance.
new_book = Book(title ='1984, author = 'George Orwell', publication_year =1949)
new_book

#Expected output :
# A Book instance is created succecfuly



# Retrieving a Book instance by title 
book = Book.objects.get(title='1984')
book

# Expected output :
# <Book: 1984>
# retrieved_book.title -> "1984"
# retrieved_book.author -> "George Orwell"
# retrieved_book.published_year -> 1949

# Updating a Book instance's title

book.title = 'Nineteen Eighty Four'
book.save.()

#Expected output :
# Expected output:
# Title updated successfully
# retrieved_book.title -> "Nineteen Eighty-Four"

# Deleting a Book instance
book.delete()
Book.objects.all()

#Expected output :
# QuerySet([])  # No books remain