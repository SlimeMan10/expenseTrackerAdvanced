from database import Database

db = Database()  # Global database instance

class User:
    def __init__(self):
        self.user_name = None

    def log_in(self):
        """Handles the user login process."""
        global db
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
        print(self.user_name)

    def create_new_user(self):
        global db
        while True:
            user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
            if not db.checkUserName(user_name): 
                break
        password = self._verify_input("Enter password: ", "Password cannot be empty")
        db.create_new_user(user_name, password)
        print("User created successfully!")
        self.user_name = user_name

    def logOut(self):
        self.user_name = None

    def _verify_input(self, prompt, error_message):
        """Validates user input."""
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print(error_message)

    def setBudget(self, budget):
        global db
        if (self.isLoggedIn()):
            db.setBudget(self.user_name, budget)
            print(f"Budget set to ${budget}!")
        else:
            print("You need to log in first.")

    def isLoggedIn(self):
        return self.user_name is not None
    
    def getCurrentBudget(self):
        global db
        if (self.isLoggedIn()):
            db.getCurrentBudget(self.user_name)
        else:
            print("You need to log in first.")