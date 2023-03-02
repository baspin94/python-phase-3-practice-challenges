from classes.order import Order

class Coffee:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Name must be a string")

    def __repr__(self):
        return f"Coffee: {self._name}"
    
    def customers(self):
        customers = []
        for order in Order.all:
            if order.coffee == self and order.customer not in customers:
                customers.append(order.customer)
        return customers

    def orders(self):
        orders = [order for order in Order.all if order.coffee == self]
        return orders
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / self.num_orders()
    
    # Property Getters
    def get_name(self):
        return self._name
    
    # Property Setters
    def name_error(self, name):
        # raise Exception(f"You can't rename this coffee to {name}.")
        pass

    # Property Definitions

    name = property(get_name, name_error)



    


    