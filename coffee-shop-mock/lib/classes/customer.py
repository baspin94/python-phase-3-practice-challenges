from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer: {self._name}"

    # Property Getters

    def get_name(self):
        return self._name

    # Property Setters
    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters.")

    # Property Definitions

    name = property(get_name, set_name)

    