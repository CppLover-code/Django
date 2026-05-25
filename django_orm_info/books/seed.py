from books.models import Book, Author, Category

# очистка таблиц
Book.objects.all().delete()
Author.objects.all().delete()
Category.objects.all().delete()

# авторы
author1 = Author.objects.create(name="Stephen King")
author2 = Author.objects.create(name="J. K. Rolling")

# Категории
horror = Category.objects.create(title="horror")
fantasy = Category.objects.create(title="fantasy")

# Книги
book1 = Book.objects.create(
    title="It",
    author = author1,
)
book2 = Book.objects.create(
    title="Harry Potter",
    author = author2
)

# ManyToMany relations
book1.categories.add(horror, fantasy)
book2.categories.add(fantasy)

print("Database seeded!")