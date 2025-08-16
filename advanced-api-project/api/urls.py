from django.urls import path

from .views import ListView, CreateView, RetrieveBooksView, UpdateView, DeleteView

urlpatterns = [
    
    path('books/', ListView.as_view(), name = 'books-list'),
    path('books/create/',CreateView.as_view(), name = 'books-create' ),
    path('books/retrieve/<pk>/',RetrieveBooksView.as_view(), name = 'books-retrieve'),
    path('books/update/<pk>/', UpdateView.as_view(), name='books-update'),
    path('books/destroy/<pk>/', DeleteView.as_view(), name='books-destroy')
    
]
