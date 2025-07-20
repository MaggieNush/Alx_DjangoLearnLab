Command
pythonfrom bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book}")
print(f"Book ID: {book.id}")
Actual Output
Book created: Book object (1)
Book ID: 1
Explanation
Successfully created a new Book instance with:

Title: "1984"
Author: "George Orwell"
Publication Year: 1949

The objects.create() method creates the instance and saves it to the database in one step. Django automatically assigns a primary key (ID) to the new record. The output shows "Book object (1)" which is the default string representation of the Book model.