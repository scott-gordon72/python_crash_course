class User:
    """A simple attempt to model a user"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializes user attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"\tUsername: {self.username}")
        print(f"\tEmail: {self.email}")
        print(f"\tLocation: {self.location}")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"\nWelcome back, {self.username} !")

    def increment_login_attempts(self):
        """Increment the value of the login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""