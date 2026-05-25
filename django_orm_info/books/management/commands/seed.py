from django.core.management.base import BaseCommand

from books.models import(Author, Book, Category)

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

        # категории
        horror = Category.objects.create(
            title="Horror"
        )

        fantasy = Category.objects.create(
            title="Fantasy"
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

        # many-to-many
        book1.categories.add(horror, fantasy)
        book2.categories.add(fantasy)

        self.stdout.write(
            self.style.SUCCESS(
                "Database seeded!"
            )
        )