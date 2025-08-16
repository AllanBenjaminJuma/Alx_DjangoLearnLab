from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.views import View

from .models import Book
from .serializers import BookSerializer

# The Views to perform CRUD operations.

"""
    A View to add new books and authors
    
"""

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
    Lists all the books
"""

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author"]
    ordering_fields = ["publication_year"]
    
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    # try using 'slug'

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    permission_classes = [IsAuthenticated]

    """This view is deletes the books.
    It uses IsAuthenticated permission to check whether the user deleting a book is authenticated in the system.
    
    """
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]