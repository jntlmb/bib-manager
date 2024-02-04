import csv


class Book:
    list_books = {}

    def __init__(self, author, title) -> None:
        self.author = author
        self.title = title
        Book.list_books[author] = title

    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author

    def get_title(self):
        return self.title
    
    def set_title(self, new_title):
        self.title = new_title

    @classmethod
    def get_books(cls):
        for author, title in Book.list_books.items():
            print(f"{author}: {title}")
            