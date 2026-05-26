from books.models import Book, Category, Author
# Для запуска
# python manage.py shell
# exec(open("test_queries.py").read())

# получить всех авторов
def get_all_authors():

    authors = Author.objects.all()

    print("All authors:")
    for author in authors:
        print(f"{author.name}\n")

# получить все книги
def get_all_books():

    books = Book.objects.all()

    print("All books:\n")
    for book in books:
        print(f"{book.title}\n")

# получить книги и их авторов
def get_book_author():

    books = Book.objects.select_related("author")

    print(f"All books with authors:\n")

    # enumerate автоматически считает номера
    for index, book in enumerate(books, start=1):
    
        print(
            f"{index}. "
            f"{book.title} - "
            f"{book.author.name}\n"
            )

# получить книги и категории
def get_book_cat():

    books = Book.objects.prefetch_related("categories")

    print(f"All books with categories:\n")

    # enumerate автоматически считает номера
    for index, book in enumerate(books, start=1):
        
        categories = ", ".join(
            category.title
            for category in book.categories.all()
        )

        print(
            f"{index}. "
            f"{book.title} - "
            f"{categories}\n"
            )
        
# получить все книги с авторами и категориями
def get_all_books_authors_cat():

    books = (
        Book.objects
        .select_related("author")
        .prefetch_related("categories")
    )

    print("All books with authors and categories:\n")

    for book in books:
        categories = ", ".join(
            category.title
            for category in book.categories.all()
        )

        print(
            f"Book title: {book.title}\n"
            f"Author: {book.author.name}\n"
            f"Categories: {categories}\n"
            f"*******************\n"
        )

# получить первую книгу
def get_first_book():

    f_book = Book.objects.first()

    print(f"First book: {f_book}\n")

# получить последнюю книгу
def get_last_book():

    l_book = Book.objects.last()

    print(f"Last book: {l_book}\n")

# получить книгу по индексу
def get_book_by_index(index):

    try:
        book = Book.objects.get(id=index)
        print(f"Book index {index} - {book.title}\n")

    except Book.DoesNotExist:
        print("Book not found!")


get_all_authors()
get_all_books()
get_book_author()
get_book_cat()
get_all_books_authors_cat()
get_first_book()
get_last_book()
# **************************
get_book_by_index(5)
get_book_by_index(10)
# **************************

"""
Также можно добавить:

* фильтрацию с разными условиями
    - По названию
    Book.objects.filter(title="Harry Potter")
    - По автору
    Book.objects.filter(author_id=1)

* проверку существования
    Book.objects.filter(id=1).exists()

* contains:
    - Поиск части текста:
    Book.objects.filter(title__contains="Python")
    - Без учёта регистра:
    Book.objects.filter(title__icontains="python")

* order_by()
    - Порядок по возрастанию
    Book.objects.order_by("title")
    - Обратный порядок
    Book.objects.order_by("-title")

* count()
    Book.objects.count()
"""



