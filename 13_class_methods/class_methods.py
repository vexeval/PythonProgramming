
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    @classmethod
    def from_dict(cls, data): # `cls` is similar to `self`
        """Create a Book object from a dictionary"""
        return cls(data["title"], data["author"], data["year"])

    @classmethod
    def reset_total_books(cls):
        cls.total_books = 0

data = {"title":"The Art of War", "author":"Sun Tzu", "year":"unknown"}
book1 = Book("Python 101", "J. Doe", 2024)
book2 = Book.from_dict(data)

print(book1.title)
print(book1.author)
print(book1.year)

print(book2.title)
print(book2.author)
print(book2.year)