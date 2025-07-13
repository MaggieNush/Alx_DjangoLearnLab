# Delete Operation

## Command
```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion by checking all books
all_books = Book.objects.all()
print(f"All books count: {all_books.count()}")
print(f"Remaining books: {all_books}")
```

## Actual Output
```
(1, {'bookshelf.Book': 1})
Book deleted successfully
All books count: 0
Remaining books: <QuerySet []>
```

## Additional Confirmation
When attempting to retrieve the deleted book:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
```

## Error Output (Proving Deletion)
```
DoesNotExist: Book matching query does not exist.
```

## Explanation
Successfully deleted the book from the database. The confirmation steps show:
1. The `delete()` method returned `(1, {'bookshelf.Book': 1})` indicating 1 object was deleted
2. The total count of books is now 0
3. The QuerySet is empty: `<QuerySet []>`
4. Attempting to retrieve the deleted book raises a `DoesNotExist` exception, confirming the deletion was successful