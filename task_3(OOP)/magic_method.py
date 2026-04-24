# Magic methods = Dunder methods (double undescore) __init__, __str__, __eq__
#                 they are automatically called by many of Python's built-in operations.
#                 they allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} {self.author} {self.num_pages}"
    
    def __eq__(self, other):
        return self.title==other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.author or keyword in self.title
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages
        else:
            return f"key '{key}' not found"

book1 = Book("One Piece", "Oda", 1181)
book2 = Book("Jujutsu Kaisen", "Gege", 345)

print(book1)
print(book1 == book2)
print(book1 > book2)
print(book1 < book2)
print(book1 + book2)
print("One" in book1)
print(book1["author"])
print(book2["title"])
print(book1["num_pages"])
print(book1["Money"])