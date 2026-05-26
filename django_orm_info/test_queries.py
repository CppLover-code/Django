from books.models import Book, Category, Author

def get_all_authors():

    authors = Author.objects.all()

    # print(authors)

    for author in authors:
        print (author.name)
        
# python manage.py shell
# exec(open("test_queries.py").read())

get_all_authors()