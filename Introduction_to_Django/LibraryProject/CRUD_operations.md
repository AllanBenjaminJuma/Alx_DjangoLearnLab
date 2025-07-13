## Create a Book instance
### Python command
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Retrieve a Book instance
### Python command
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)

print(book.title, book.author, book.publication_year)

## Update a Book instance
### Python command

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title, book.author, book.publication_year)
Nineteen Eighty-Four George Orwell 1949

## Delete a Book instance
### Python command
book.delete()
(1, {'bookshelf.Book': 1}) 