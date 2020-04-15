class User:
    """A simple attempt to model a user"""

    def __init__(self, first_name, last_name, age, height, weight):
        """Initializes user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"\nFirst name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
        print("How are you today?")


connor = User('connor', 'gordon', 17, 71, 250)
scott = User('scott', 'gordon', 48, 72, 285)
lisa = User('lisa', 'gordon', 47, 68, 230)

connor.describe_user()
connor.greet_user()
scott.describe_user()
scott.greet_user()
lisa.describe_user()
lisa.greet_user()
