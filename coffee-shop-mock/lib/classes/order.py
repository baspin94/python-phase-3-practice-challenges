# from classes.customer import Customer

class Order:
    
    all = []
    
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.add_to_all(self)
    
    def __repr__(self):
        return f"{self._customer} {self.coffee} Price: {self.price}"
    
    @classmethod
    def add_to_all(cls, order):
        cls.all.append(order)

    # Property Getters
    def get_price(self):
        return self._price
    
    def get_customer(self):
        return self._customer
    
    def get_coffee(self):
        return self._coffee

    # Property Setters
    def set_price(self, price):
        if isinstance(price, int) and (1 <= price <= 10):
            self._price = price

    def set_customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            pass

    def set_coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            pass

    # Property Definitions
    price = property(get_price, set_price)
    customer = property(get_customer, set_customer)
    coffee = property(get_coffee, set_coffee)
