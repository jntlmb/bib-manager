from Customer import Customer
from Book import Book

class Order(Customer, Book):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)

# nicht aktuell
def place_order(self, *books):
        for book in books:
            if len(book) != 2:
                print("Unknown Book format.")
            else:
                author, title = book
                title_list = self.orders.values()

                if title in title_list:
                    print(f'Book already ordered: "{author}: {title}"')
                else:
                    self.orders[author] = title
                    print(f'Order success: "{author}: {title}"')