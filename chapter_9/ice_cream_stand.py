class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Prints the restaurants name, cuisine type and indicates if open"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurants name and cusine type"""
        print(f"{self.restaurant_name.title()} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open")


class IceCreamStand(Restaurant):
    """
    IceCreamStand restaurant class, which models real-world Ice Cream Stand restaurant.
    """

    def __init__(self, restaurant_name, cousine_type='ice cream'):
        """
        Initialize parent class attributes and add IceCreamStand specific attributes.
        """
        super().__init__(restaurant_name, cousine_type)
        self.flavors = ['strawberry', 'vanilla', 'malaga',
                        'chocolate', 'blackberry', 'annanas', ]

    def display_flavors(self):
        """Method that displays list of flavors"""
        print(
            f"The restaurant {self.restaurant_name.title()} can offer next ice cream flavors:")
        for flavor in self.flavors:
            print(f"-{flavor}")


ice_car = IceCreamStand('dolly')
ice_car.display_flavors()
