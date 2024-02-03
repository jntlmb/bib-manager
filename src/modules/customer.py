class Customer:
    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email
        self.orders = {}

    def get_username(self):
        return self.username
    
    def set_username(self, new_username):
        self.username = new_username

    def get_email(self):
        return self.email
    
    def set_email(self, new_email):
        self.email = new_email

    def update_username(self, old_username, new_username):
        if old_username != self.username:
            return False
        else:
            self.set_username(new_username)
            return True

    def update_email(self, old_email, new_email):
        if old_email != self.email:
            return False
        else:
            self.set_email(new_email)
            return True
        
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


    def view_oders(self):
        if len(self.orders) == 0:
            print("No open Orders.")
        else:
            for o in self.orders:
                print(f"{o}: {self.orders[o]}")
        

customer1 = Customer("test_user", "test_email")
customer1.place_order(("George Orwell", "1984", "Fiction"))

customer1.place_order(("George Orwell", "1984"))
customer1.view_oders()

customer1.place_order(("George Orwell", "1984"))