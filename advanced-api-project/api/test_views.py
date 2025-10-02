from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="J.K. Rowling")

        # Create books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author1)
        self.book3 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author2)

        self.client = APIClient()

    # ---------- CRUD TESTS ----------

    def test_list_books(self):
        """Anyone can list books"""
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book(self):
        """Anyone can retrieve a single book"""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books"""
        url = reverse("book-create")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated_force_auth(self):
        """Authenticated users can create books using force_authenticate"""
        self.client.force_authenticate(user=self.user)
        url = reverse("book-create")
        data = {"title": "Homage to Catalonia", "publication_year": 1938, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_authenticated_login(self):
        """Authenticated users can create books using login()"""
        logged_in = self.client.login(username="testuser", password="password123")
        self.assertTrue(logged_in)  # make sure login worked
        url = reverse("book-create")
        data = {"title": "Keep the Aspidistra Flying", "publication_year": 1936, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5)
        self.client.logout()

    def test_update_book_authenticated(self):
        """Authenticated users can update a book"""
        self.client.login(username="testuser", password="password123")
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")
        self.client.logout()

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username="testuser", password="password123")
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
        self.client.logout()

    # ---------- FILTER, SEARCH, ORDER TESTS ----------

    def test_filter_books_by_author(self):
        url = reverse("book-list") + f"?author={self.author1.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Harry"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Harry Potter")

    def test_order_books_by_year(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Harry Potter")

# Notes:
# Tests cover:
# - CRUD: Create, Retrieve, Update, Delete
# - Permissions: Unauthenticated users cannot modify data
# - Filtering: ?author=<id>
# - Searching: ?search=<keyword>
# - Ordering: ?ordering=<field>
#
# Run tests:
# python manage.py test api