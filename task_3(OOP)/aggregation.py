# Aggregation = Represents a relationship where one object (the whole)
#                 contains references to one or more INDEPENDENT objects (the parts)
#the classes can exist without eachother
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def list_book(self):
        return [f'{book.title} by {book.author}'for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library('World History Library')

book1 = Book('Heaven\'s steps', 'Yohan Doe')
book2 = Book('Secret world', 'Jane Doe')

library.add_books(book1)
library.add_books(book2)


print(library.name)
for book in library.list_book():
    print(book)



