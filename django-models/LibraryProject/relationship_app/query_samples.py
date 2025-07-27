from relationship_app.models import Author, Book, Librarian, Library

### query books by a specific author
def book_by_author(author_name):
    try:
        author = Author.objects.get(name = author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"-{book.title}")
    except Author.DoesNotExist:
        print(f"No author found by the name '{author_name}'.")
        
### list all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name} Library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library named '{library_name}'.")

### Librarian for a library

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")
    
if __name__ == "__main__":
    book_by_author("Allan Juma")
    books_in_library("Main Library")
    librarian_for_library("West Library")