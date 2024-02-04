class Customer:
    list_customer = {}

    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email
        Customer.list_customer[username] = email

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

    @classmethod
    def view_customer(self):
        if len(Customer.list_customer) == 0:
            print("No Customers Registered.")
        else:
            for username, email in Customer.list_customer.items():
                print(f"{username}: {email}")
        

customer1 = Customer("test_user", "test_email")
customer2 = Customer("test_user1", "test_email1")
Customer.view_customer()