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


class Admin(User):
    """Admin user class, which models real-world admin"""

    def __init__(self, first_name, last_name, age, height, weight):
        """
        Initialize parent class attributes and Admin specific attributes
        """
        super().__init__(first_name, last_name, age, height, weight)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Method to show privileges allowed to the admin"""
        print(f"\n{self.first_name} has these privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")


admin = Admin('scott', 'gordon', 48, 72, 285)
admin.show_privileges()