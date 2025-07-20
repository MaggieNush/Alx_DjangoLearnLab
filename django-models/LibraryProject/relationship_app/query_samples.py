import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

from models import Author, Book, Library, Librarian

def query_all_books_by_author():
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name='Stephen King')
        books = author.book_set.all()

        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author not found")

def list_all_books_in_library():
    """List all books in a library"""
    try:
        library = Librarian.objects.get(name='City Library')
        books = library.books.all()

        print(f"Books in {library.name}:")
        for book in books:
            print(f"-{book.title}")
    except Library.DoesNotExist:
        print("Library not found")

def retrieve_librarian_for_library():
    """Retrieve librarian for library"""
    try:
        library = Library.objects.get(name='City Library')
        librarian = library.librarian

        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found")
    except Librarian.DoesNotExist:
        print("No librarian assigned to the library")

if __name__ == "__main__":
    query_all_books_by_author
    print('-------------------------')
    list_all_books_in_library
    print('-------------------------')
    retrieve_librarian_for_library
    print('-------------------------')
    
