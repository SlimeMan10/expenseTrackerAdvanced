class UsernameAlreadyExistsError(Exception):
    """Exception raised when a username already exists in the database."""
    def __init__(self, username, message="Username is already taken."):
        self.username = username
        self.message = message
        super().__init__(f"{message} Username: {username}")