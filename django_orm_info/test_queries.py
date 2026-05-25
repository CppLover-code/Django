from books.models import Book, Category, Author

def get_all_authors():

    authors = Author.objects.all()

    print(authors)

"""
def main():
    print("DB TEST:\n")
    get_all_authors()
"""
get_all_authors()