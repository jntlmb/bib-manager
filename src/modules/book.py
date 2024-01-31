import csv


class Book:
    titles = []

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        Book.titles.append(self.title)

    def write_books_in_csv(self):
        with open('books.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(["Title", "Author", "Genre"])

            if self.title in Book.titles:
                return print("Book is already in Library")
            else:
                writer.writerow([self.title, self.author, self.genre])
