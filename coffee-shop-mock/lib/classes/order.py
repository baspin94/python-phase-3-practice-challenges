
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    
    def __repr__(self):
        return f"{self.customer} {self.coffee} Price: {self.price}"
    
    # Property Getters
    def get_price(self):
        return self._price

    # Property Setters
    def set_price(self, price):
        if isinstance(price, int) and (1 <= price <= 10):
            self._price = price

    # Property Definitions
    price = property(get_price, set_price)
