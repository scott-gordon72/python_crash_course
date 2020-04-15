class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Prints the restaurants name, cuisine type and indicates if open"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the restaurants name and cusine type"""
        print(f"{self.restaurant_name.title()} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open")

    def set_number_served(self, served):
        """Sets the number of customers who have been served"""
        self.number_served = served

    def increment_number_served(self, served_today):
        """Increment the number of customers that have been served"""
        self.number_served += served_today


restaurant = Restaurant('il camino', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"The number of customers served is: {restaurant.number_served}")
restaurant.number_served = 12
print(f"The number of customers served is: {restaurant.number_served}")
restaurant.set_number_served(18)
print(f"The number of customers served is: {restaurant.number_served}")
restaurant.increment_number_served(10)
print(f"The number of customers served is: {restaurant.number_served}")
