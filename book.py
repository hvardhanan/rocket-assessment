from enums import BookStatus

class Book:
    def __init__(self, id, isbn, title, author, quantity):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
        self.status = BookStatus.AVAILABLE if quantity > 0 else BookStatus.ISSUED
