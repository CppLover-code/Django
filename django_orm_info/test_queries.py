from books.models import Book, Category, Author
# Для запуска
# python manage.py shell
# exec(open("test_queries.py").read())

# получить всех авторов
def get_all_authors():

    authors = Author.objects.all()

    for author in authors:
        print(author.name)

# получить все книги
def get_all_books():

    books = Book.objects.all()

    for book in books:
        print(book.title)

# получить все книги с авторами
def get_all_books_authors():

    books = Book.objects.all()

    for book in books:
        print(f"Book title: {book.title}\nAuthor: {book.author}\nCategory: {','.join(map(lambda c: c.title, book.categories.all()))}\n***********\n")

get_all_authors()
get_all_books()
get_all_books_authors()

