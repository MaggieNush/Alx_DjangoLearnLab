# CRUD Operations Documentation

This file documents all CRUD operations performed on the Book model in the Django shell.

## Prerequisites
- Django project with bookshelf app
- Book model properly defined in models.py
- Migrations applied successfully

## Shell Session Commands

### Opening Django Shell
```bash
python manage.py shell
```

### Import Statement
```python
from bookshelf.models import Book
```

---

## CREATE Operation

### Command:
```python
# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book}")
print(f"Book ID: {book.id}")
```

### Actual Output:
```
Book created: Book object (1)
Book ID: 1
```

### Notes:
- Successfully created a new Book instance with specified attributes
- Django automatically assigned primary key ID = 1
- The `objects.create()` method creates and saves the instance in one step
- Output shows "Book object (1)" which is the default string representation

---

## RETRIEVE Operation

### Command:
```python
# Retrieve the book we just created
book = Book.objects.get(title="1984")
print(f"Retrieved book: {book}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
```

### Actual Output:
```
Retrieved book: Book object (1)
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
```

### Notes:
- Successfully retrieved the book using the title as lookup parameter
- All attributes are accessible via dot notation
- The `get()` method returns exactly one object
- "Book object (1)" confirms this is the instance with ID 1

---

## UPDATE Operation

### Command:
```python
# Update the book's title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated book: {book}")
print(f"New title: {book.title}")
```

### Actual Output:
```
Updated book: Book object (1)
New title: Nineteen Eighty-Four
```

### Notes:
- Successfully updated the book's title from "1984" to "Nineteen Eighty-Four"
- The `save()` method persists changes to the database
- Other attributes (author, publication_year) remain unchanged
- Same instance ID (1) confirms we updated the existing record

---

## DELETE Operation

### Command:
```python
# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion by checking all books
all_books = Book.objects.all()
print(f"All books count: {all_books.count()}")
print(f"Remaining books: {all_books}")
```

### Actual Output:
```
(1, {'bookshelf.Book': 1})
Book deleted successfully
All books count: 0
Remaining books: <QuerySet []>
```

### Additional Confirmation:
When attempting to retrieve the deleted book:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
```

### Error Output (Proving Deletion):
```
DoesNotExist: Book matching query does not exist.
```

### Notes:
- Successfully deleted the book using the `delete()` method
- Delete operation returned `(1, {'bookshelf.Book': 1})` indicating 1 object was deleted
- Confirmed deletion by checking the total count (0) and empty QuerySet
- The `DoesNotExist` exception when trying to retrieve confirms the book no longer exists

---

## Summary

All CRUD operations were successfully completed:

1. **CREATE**: Created a Book instance with title "1984", author "George Orwell", publication year 1949
2. **RETRIEVE**: Retrieved the book and displayed all its attributes
3. **UPDATE**: Modified the title from "1984" to "Nineteen Eighty-Four"
4. **DELETE**: Removed the book from the database and confirmed deletion

The Django ORM successfully handled all database operations, demonstrating proper integration between the model and database schema. The default string representation "Book object (1)" indicates the model's `__str__` method could be improved for better readability in future development.