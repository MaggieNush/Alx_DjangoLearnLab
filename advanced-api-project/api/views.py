from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.core.exceptions import PermissionDenied

class BookListView(generics.ListAPIView):
    """
    View to retrieve all books.
    This view uses the BookSerializer to serialize the book data.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new model instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return super().perform_create(serializer)(self, serializer)
    
    # Only authenticated users can create a book
        if not self.request.user.has_perm('api.add_book'):
            raise PermissionDenied("You do not have permission to create a book.")

        serializer.save(author=self.request.user)  

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Example: Only allow users with a specific permission
        if not self.request.user.has_perm('api.change_book'):
            raise PermissionDenied("You do not have permission to update this book.")
        serializer.save()

    def get_queryset(self):
        # Example: Only allow users to update books they created
        return Book.objects.filter(created_by=self.request.user)

class BookDeleteView(generics.DestroyAPIView):
    """
    View to remove a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can delete a book
