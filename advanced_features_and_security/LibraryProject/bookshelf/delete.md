from bookshelf.models import Book

book.delete()
Book.objects.all()

#Expected output :
# QuerySet([])  # No books remain