book = Book.objects.get(title='1984')
book

# Expected output :
# <Book: 1984 by George Orwell (1949)>
# retrieved_book.title -> "1984"
# retrieved_book.author -> "George Orwell"
# retrieved_book.published_year -> 1949
