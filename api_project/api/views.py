from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer