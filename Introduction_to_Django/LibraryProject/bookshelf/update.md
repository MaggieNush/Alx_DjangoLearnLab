# Update Operation

## Command
```python
from bookshelf.models import Book

# Retrieve and update the book's title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated book: {book}")
print(f"New title: {book.title}")
```

## Actual Output
```
Updated book: Book object (1)
New title: Nineteen Eighty-Four
```

## Explanation
Successfully updated the book's title from "1984" to "Nineteen Eighty-Four". The process involved:
1. Retrieving the existing book instance
2. Modifying the title attribute
3. Calling `save()` to persist the changes to the database

The book's other attributes (author and publication year) remain unchanged. The output shows "Book object (1)" confirming it's the same instance with ID 1.