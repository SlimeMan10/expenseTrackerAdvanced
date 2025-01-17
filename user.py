from database import Database

db = Database()  # Global database instance
user = None  # Global user instance

class User:
    def __init__(self):
        self.user_name = None

    def log_in(self):
        """Handles the user login process."""
        global db
        global user
        user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
        password = self._verify_input("Enter your password: ", "Password cannot be empty")

        while True:
            condition = db.logIn(user_name, password)
            if condition == 0:
                self.user_name = user_name
                print(f"Welcome, {user_name}!")
                break
            elif condition == 1:
                user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
            else:
                password = self._verify_input("Enter your password: ", "Password cannot be empty")
        print("Logged in successfully!")
        user = user_name

    def create_new_user(self):
        global db
        global user
        while True:
            user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
            if not db.checkUserName(user_name): 
                break
        password = self._verify_input("Enter password: ", "Password cannot be empty")
        db.create_new_user(user_name, password)
        print("User created successfully!")
        user = user_name

    def _verify_input(self, prompt, error_message):
        """Validates user input."""
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print(error_message)
