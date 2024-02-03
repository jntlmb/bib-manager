from Customer import Customer

class Order(Customer):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)