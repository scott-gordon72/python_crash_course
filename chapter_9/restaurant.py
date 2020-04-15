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


restaurant = Restaurant('il camino', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
