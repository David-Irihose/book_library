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