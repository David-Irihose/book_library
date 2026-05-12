import json


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

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "borrowed": self.borrowed
        }

    def save(self):

        try:

            with open("books.json", "r") as file:
                data = json.load(file)

        except:

            data = []

        data.append(self.to_dict())

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Book saved")


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

book1.save()