from user import User
from admin import Admin
from database import Database

db = Database()  # Global database instance

userTotalChoices = 5
adminTotalChoices = 11

class Connection:
    def __init__(self):
        self.user = None
        self.admin = None

    def start(self):
        while True:
            self.__printOptions()
            try:
                choice = int(input("Choice: "))
                totalChoices = userTotalChoices if self.user else adminTotalChoices
                if choice == 0:
                    self.logOut()
                    break
                if choice < 0 or choice > totalChoices:
                    raise ValueError
            except ValueError:
                print("Enter a valid choice")
                print()
                continue
            self.__checkOptions(choice)

    def __checkOptions(self, choice):
        if self.user:
            self.__userOptions(choice)
        else:
            self.__adminOptions(choice)

    def __userOptions(self, choice):
        if choice == 0:
            print("Exiting the user. Goodbye!")
            self.user = None
        else:
            self.__sharedOptions(choice)

    def __adminOptions(self, choice):
        if choice == 0:
            print("Exiting the admin. Goodbye!")
            self.admin = None
        elif choice in range(1, 6):  # Admin also has access to user options
            self.__sharedOptions(choice)
        elif choice == 6:
            self.admin.setNewBudget()
        elif choice == 7:
            self.admin.deleteUser()  # Assuming there's a `deleteUser` method
        elif choice == 8:
            self.admin.makeNewAdmin()  # Assuming there's a `makeNewAdmin` method
        elif choice == 9:
            self.admin.viewAllUsers()  # Assuming there's a `viewAllUsers` method
        elif choice == 10:
            self.admin.addNewCategory()  # Assuming there's an `addNewCategory` method
        elif choice == 11:
            self.admin.viewSpendingHistory()  # Assuming there's a `viewSpendingHistory` method
        else:
            print("Invalid choice for admin.")

    def __sharedOptions(self, choice):
        """Shared functionality for both users and admins."""
        if choice == 1:
            if self.user:
                self.user.getCurrentBudget()
            elif self.admin:
                self.admin.getCurrentBudget()
        elif choice == 2:
            if self.user:
                self.user.getCurrentSpending()
            elif self.admin:
                self.admin.getCurrentSpending()
        elif choice == 3:
            if self.user:
                self.user.addExpense()
            elif self.admin:
                self.admin.addExpense()
        elif choice == 4:
            if self.user:
                self.user.reviewAllExpenses()
            elif self.admin:
                self.admin.reviewAllExpenses()
        elif choice == 5:
            if self.user:
                self.user.reviewExpensesByCategory()
            elif self.admin:
                self.admin.reviewExpensesByCategory()

    def __printOptions(self):
        """Prints available options based on login state."""
        if self.user:
            print("0. Logout")
            print("1. Get Current Budget")
            print("2. Get Current Spending")
            print("3. Add New Expense")
            print("4. Review All Expenses")
            print("5. Review Category Expenses")
        elif self.admin:
            print("0. Logout")
            print("1. Get Current Budget")
            print("2. Get Current Spending")
            print("3. Add New Expense")
            print("4. Review All Expenses")
            print("5. Review Category Expenses")
            print("6. Set New Budget")
            print("7. Delete User")
            print("8. Make New Admin")
            print("9. View All Users")
            print("10. Add New Category")
            print("11. View All Spending History")
        else:
            print("Login first.")

    def logIn(self):
        """Handles the user login process."""
        global db
        user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
        password = self._verify_input("Enter your password: ", "Password cannot be empty")
        while True:
            condition = db.logIn(user_name, password)
            if condition == 0:
                print(f"Welcome, {user_name}!")
                break
            elif condition == 1:
                user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
            else:
                password = self._verify_input("Enter your password: ", "Password cannot be empty")
        adminOrNot = db.checkIfAdmin(user_name)
        if adminOrNot:
            self.admin = Admin(user_name)
            print("You are an admin!")
        else:
            self.user = User(user_name)
            print("You are a regular user!")

    def signUp(self):
        global db
        while True:
            user_name = self._verify_input("Enter your username: ", "Username cannot be empty")
            if not db.checkUserName(user_name): 
                break
        password = self._verify_input("Enter password: ", "Password cannot be empty")
        db.create_new_user(user_name, password)
        print("User created successfully!")
        self.user = User(user_name)

    def _verify_input(self, prompt, error_message):
        """Validates user input."""
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print(error_message)

    def logOut(self):
        """Logs out the current user or admin."""
        if self.user:
            self.user = None
        elif self.admin:
            self.admin = None
        print("Logged out successfully!")
        print("Goodbye!")

    def getCurrentBudget(self):
        """Gets the current budget of the logged-in user/admin."""
        if self.user:
            self.user.getCurrentBudget()
        elif self.admin:
            self.admin.getCurrentBudget()

    def getCurrentSpending(self):
        """Gets the current spending of the logged-in user/admin."""
        if self.user:
            self.user.getCurrentSpending()
        elif self.admin:
            self.admin.getCurrentSpending()