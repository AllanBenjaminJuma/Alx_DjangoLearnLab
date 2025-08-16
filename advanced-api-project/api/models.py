from django.db import models
import datetime

"""
    Represents an Author.
    
"""
class Author(models.Model):
    name = models.CharField(max_length=200)

"""
    Represents a Book.
    Fields:
        title(str): The title of the book.
        publication_year(int): The publication year of the book.
        author(str): The author of the book 
    
"""
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(default=2025)
    author = models.ManyToManyField(Author)