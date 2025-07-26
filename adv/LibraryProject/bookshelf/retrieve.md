# Retrieve Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book we just created
book = Book.objects.get(title="1984")
print(f"Retrieved book: {book}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
```

## Actual Output
```
Retrieved book: Book object (1)
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
```

## Explanation
Successfully retrieved the book from the database using the `get()` method with the title as the lookup parameter. The output shows all attributes of the retrieved Book instance, including the auto-generated ID field. The "Book object (1)" indicates this is the Book instance with ID 1.