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

    print("All books:")
    for book in books:
        print(f"{book.title}\n")

# получить все книги с авторами и категориями
def get_all_books_authors():

    books = Book.objects.all()
    print("All books with authors and categories:")
    for book in books:
        print(f"Book title: {book.title}\nAuthor: {book.author}\nCategory: {','.join(map(lambda c: c.title, book.categories.all()))}\n***********\n")

# получить первую книгу
def get_first_book():

    f_book = Book.objects.first()

    print(f"First book: {f_book}\n")

# получить последеюю книгу
def get_last_book():

    l_book = Book.objects.last()

    print(f"First book: {l_book}\n")

get_all_authors()
get_all_books()
get_all_books_authors()
get_first_book()
get_last_book()


