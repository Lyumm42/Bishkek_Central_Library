from django.test import TestCase
from .models import Book, Author

class SimpleBookTest(TestCase):
    def test_create_author_and_book(self):
        author = Author.objects.create(name="Тест Автор")
        book = Book.objects.create(title="Тест Книга", author=author, total_copies=3, available_copies=3)
        self.assertEqual(str(book), "Тест Книга")
        self.assertEqual(book.author.name, "Тест Автор")
