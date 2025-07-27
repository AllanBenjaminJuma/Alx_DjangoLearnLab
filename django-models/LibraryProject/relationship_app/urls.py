from django.urls import path
from .views import all_books_view, LibraryDetailView

urlpatterns = [
    path('books/', all_books_view, name='list_books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detail')
]
