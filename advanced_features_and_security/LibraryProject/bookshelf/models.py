from django.db import models

# Create your models here.
# add the book
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title

# retrieve the book from the db
class RetrieveBook(models.Model):
    