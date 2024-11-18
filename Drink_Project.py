# Class to represent a Drink, which has a base and flavors
class Drink:
    # List of possible valid bases and flavors (these don't change)
    _valid_bases = ["water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"]
    _valid_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]

    def __init__(self, base):
        # Private variables for the base and flavors
        self._base = None
        self._flavors = []

        # Set the base if it's valid
        if base in Drink._valid_bases:
            self._base = base
        else:
            raise ValueError("Invalid base")

    # Getter for the base of the drink
    def get_base(self):
        return self._base

    # Getter for the list of flavors
    def get_flavors(self):
        return self._flavors

    # Getter for the number of flavors
    def get_num_flavors(self):
        return len(self._flavors)

    # Add a flavor to the drink
    def add_flavor(self, flavor):
        # Ensure that the flavor is valid and isn't already in the list
        if flavor not in Drink._valid_flavors:
            raise ValueError("Invalid flavor")
        if flavor not in self._flavors:
            self._flavors.append(flavor)
        else:
            print(f"Flavor '{flavor}' is already added.")

    # Set the list of flavors (replaces existing flavors)
    def set_flavors(self, flavors):
        # Check that the flavors are valid and don't have duplicates
        for flavor in flavors:
            if flavor not in Drink._valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}")
        self._flavors = list(set(flavors))  # Remove duplicates by converting to a set

# Class to represent an Order which contains multiple drinks
class Order:
    def __init__(self):
        # Private list to store drinks
        self._items = []

    # Getter for the list of items in the order
    def get_items(self):
        return self._items

    # Getter for the total price of the order (we'll assume a fixed price for simplicity)
    def get_total(self):
        total = 0
        for drink in self._items:
            total += 5  # Assume each drink costs 5 for simplicity (you can add price logic here)
        return total

    # Getter for the number of items in the order
    def get_num_items(self):
        return len(self._items)

    # Getter for the receipt (returns a string summary of the order)
    def get_receipt(self):
        receipt = "Receipt:\n"
        for i, drink in enumerate(self._items):
            receipt += f"Drink {i + 1}: Base = {drink.get_base()}, Flavors = {', '.join(drink.get_flavors())}\n"
        receipt += f"Total: ${self.get_total()}"
        return receipt

    # Add a drink to the order
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise ValueError("Item must be a Drink object")

    # Remove a drink from the order by index
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]
        else:
            raise IndexError("Item index out of range")
