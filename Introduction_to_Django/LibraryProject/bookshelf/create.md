from bookshelf.models import Book

#creating a Book instance.
new_book = Book.objects.create(title ='1984', author = 'George Orwell', publication_year =1949)


#Expected output :
# A Book instance is created succecfuly
<Book: 1984 by George Orwell (1949)>