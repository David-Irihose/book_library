import json
import datetime


class BaseLine:

    def __init__(self, id):

        self.id = id
        self.created_at = str(datetime.datetime.now())
        self.updated_at = str(datetime.datetime.now())

    def touch(self):

        self.updated_at = str(datetime.datetime.now())


class Book(BaseLine):

    def __init__(self, id, title, author, year, genre, borrowed=False, borrowed_by=None):

        super().__init__(id)

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.borrowed = borrowed
        self.borrowed_by = borrowed_by

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "borrowed": self.borrowed,
            "borrowed_by": self.borrowed_by,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def save(self):

        try:

            with open("books.json", "r") as file:
                data = json.load(file)

            if type(data) != dict:
                data = {}

        except:

            data = {}

        key = f"book{self.id}"

        data[key] = self.to_dict()

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

        print(f"{self.title} saved")

    @classmethod
    def load(cls):

        with open("books.json", "r") as file:
            data = json.load(file)

        books = []

        for key, item in data.items():

            book = cls(
                item["id"],
                item["title"],
                item["author"],
                item["year"],
                item["genre"],
                item["borrowed"],
                item["borrowed_by"]
            )

            books.append(book)

        return books

    def __str__(self):

        return f"{self.title} by {self.author}"


class User(BaseLine):

    def __init__(self, id, name):

        super().__init__(id)

        self.name = name

    def borrow(self, book):

        if book.borrowed:

            print("Book not available")

        else:

            book.borrowed = True
            book.borrowed_by = self.name

            book.touch()

            print(f"{self.name} borrowed {book.title}")

            book.save()


book1 = Book(1, "Rich Dad Poor Dad", "Robert Kiyosaki", 2001, "Finance")

book2 = Book(2, "Atlas", "Kibonangoma", 2013, "Geography")

book1.save()
book2.save()

user1 = User(1, "Alice")

user1.borrow(book1)

books = Book.load()

for b in books:

    print(b.title)
    print(b.borrowed_by)