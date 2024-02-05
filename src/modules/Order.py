from Customer import Customer
from Book import Book

class Order(Customer, Book):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)
                    