from django.core.management.base import BaseCommand

from books.models import(Author, Book, Category)

"""
в Django обычно сиды делают через custom command:
Структура:

books/
└── management/
    └── commands/
        └── seed.py

Запуск: python manage.py seed
"""
class Command(BaseCommand):

    help = "Seed database with test data"

    def handle(self, *args, **kwargs):
        
        # очистка
        Book.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()

        # авторы
        author1 = Author.objects.create(
            name="Stephen King"
        )

        author2 = Author.objects.create(
            name="J. K. Rowling"
        )
        author3 = Author.objects.create(
            name="William Shakespeare"
        )

        # категории
        horror = Category.objects.create(
            title="Horror"
        )

        fantasy = Category.objects.create(
            title="Fantasy"
        )

        romance = Category.objects.create(
            title="Romance"
        )

        # книги
        book1 = Book.objects.create(
            title="It",
            author=author1
        )

        book2 = Book.objects.create(
            title="Harry Potter",
            author=author2
        )
        book3 = Book.objects.create(
            title="Romeo and Juliet",
            author=author3
        )

        # many-to-many
        book1.categories.add(horror, fantasy)
        book2.categories.add(fantasy)
        book3.categories.add(romance)

        self.stdout.write(
            self.style.SUCCESS(
                "Database seeded!"
            )
        )