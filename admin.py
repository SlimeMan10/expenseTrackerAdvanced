from user import User
from database import Database

db = Database()  # Global database instance

class Admin(User):

    def __init__(self, username):
        super().__init__(username)

    def setNewBudget(self):
        if self.isLoggedIn():
            username = self.checkIfAllUsers()
            budget = self.__getBudgetAmount()
            if username:
                db.setBudget(username, budget)
            else:
                db.setBudget(None, budget)
        else:
            print("You need to log in first.")

    def __getBudgetAmount(self):
        while True:
            try:
                budget = float(input("Enter the new budget: "))
                if budget < 0:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid positive number")
                print()
        return budget
    
    def checkIfAllUsers(self):
        print("Do you want to set a budget for all users? (y/n)")
        choice = input().lower()
        if choice == 'y':
            return None
        return self.__getSpecificUser()

    def deleteUser(self):
        if self.isLoggedIn():
            username = self.__getSpecificUser()
            if username:
                db.deleteUser(username)
            else:
                print("No user selected.")
        else:
            print("You need to log in first.")

    def __getSpecificUser(self):
        users = self.__getAllUsers()
        while True:
            try:
                choice = input("Do you want a specific user? (y/n)").lower()
                if choice == 'n':
                    return None
                if choice == 'y':
                    break
                raise ValueError
            except ValueError:
                print("Enter 'y' or 'n'")
                print()
        while True:
            try:
                user_index = int(input("Enter the user number: (or 0 to cancel): "))
                if user_index == 0:
                    return None
                if user_index < 1 or user_index > len(users):  # Corrected to start from 1
                    raise ValueError
                return users[user_index-1][0]  # Return the username string, not the tuple
            except ValueError:
                print(f"Number must be between 1 and {len(users)}.")
                print()

    def makeNewAdmin(self):
        if self.isLoggedIn():
            username = self.__getSpecificUser()
            if username:
                db.makeNewAdmin(username)
            else:
                print("No user selected.")
        else:
            print("You need to log in first.")

    def getAllUsers(self):
        if self.isLoggedIn():
            return self.__getAllUsers()
        else:
            print("You need to log in first.")

    def __getAllUsers(self):
        users = db.getAllUsers()  # Assume this returns a list of tuples like [('user1',), ('user2',),...]
        if len(users) == 0:
            print("No users found in the database.")
            return None
        for i in range(len(users)):
            print(f"{i+1}. {users[i][0]}")  # Extract the username string from the tuple
        return users
    
    def addNewCategory(self, category):
        if self.isLoggedIn():
            category = input("Enter the new category: ")
            db.addNewCategory(category)
        else:
            print("You need to log in first.")

    def viewSpendingHistory(self):
        if self.isLoggedIn():
            user = self.__getSpecificUser()
            if user:
                data = db.viewAllSpendingHistory(user)
            else:
                data = db.viewAllSpendingHistory()
            if data:
                print("Spending history:")
                for row in data:
                    print(f"Category: {row[0]}, username: {row[1]}, item: ${row[2]}, price: ${row[3]}")
        else:
            print("You need to log in first.")

