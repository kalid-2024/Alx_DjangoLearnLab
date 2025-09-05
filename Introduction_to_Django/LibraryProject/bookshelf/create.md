from bookshelf.models import Book

#creating a Book instance.
new_book = Book(title ='1984, author = 'George Orwell', published_year =1949)
new_book.save()

#Expected output :
# A Book instance is created succecfuly
<Book: 1984 by George Orwell (1949)>