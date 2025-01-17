from user import User

# Categories: food, transport, shopping, entertainment, travel, technology, social
class Tracker:
    # Initialize with a default budget of 1000 (whole number)
    def __init__(self):
        self.user = User()

    def getCurrentBudget(self):
        """Get the current budget for the logged-in user."""
        self.user.getCurrentBudget()

    def getCurrentSpending(self):
        self.user.getCurrentSpending()

    def logIn(self):
        self.user.log_in()
    
    def signUp(self):
        self.user.create_new_user()

    def logOut(self):
        self.user.logOut()