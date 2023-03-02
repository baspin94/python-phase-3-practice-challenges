from classes.order import Order

class Coffee:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Name must be a string")

    def __repr__(self):
        return f"Coffee: {self._name}"
    
    # Property Getters
    def get_name(self):
        return self._name
    
    # Property Setters
    def name_error(self, name):
        raise Exception(f"You can't rename this coffee to {name}.")

    # Property Definitions

    name = property(get_name, name_error)



    


    