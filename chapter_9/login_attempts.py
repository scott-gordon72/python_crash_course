class User:
    """A simple attempt to model a user"""

    def __init__(self, first_name, last_name, age, height, weight):
        """Initializes user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increments the login attempts by the user"""
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        """Resets the number of login attempts to zero"""
        self.login_attempts = 0
        return self.login_attempts


scott = User('scott', 'gordon', 48, 72, 285)
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")
print(f"Login attempt: {scott.increment_login_attempts()}")

print(f"Resetting login attempts:")
scott.reset_login_attempts()
print(f"Login attempt: {scott.login_attempts}")
