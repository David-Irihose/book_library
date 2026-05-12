class BaseLine:

    def __init__(self, id):
        self.id = id


class Book(BaseLine):

    def __init__(self, id, title, author, year, genre):
        super().__init__(id)

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.borrowed = False


class User(BaseLine):

    def __init__(self, id, name):
        super().__init__(id)

        self.name = name

    
    def borrow(self, book):

        if book.borrowed:

            print("Book not available")

        else:

            book.borrowed = True

            print(f"{self.name} borrowed {book.title}")


book1 = Book(1, "Rich Dad Poor Dad", "Robert Kiyosaki", 2001, "Finance")

user1 = User(1, "Alice")

user1.borrow(book1)