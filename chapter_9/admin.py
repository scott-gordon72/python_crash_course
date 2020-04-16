from privileges import Privileges
from user import User


class Admin(User):
    """A user with admin privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges
        self.privileges = Privileges()
