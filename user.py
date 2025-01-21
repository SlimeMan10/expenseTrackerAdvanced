from database import Database

db = Database()  # Global database instance

class User:
    def __init__(self, userName):
        self.user_name = userName

    def addExpense(self):
        categories = db.getAllCategories()
        length = len(categories)
        for i in range(length):
            print(f"{i+1}. {categories[i]}")
        while True:
            try:
                category_index = int(input("Enter the category number: "))
                if category_index < 0 or category_index > length:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid number (0 to 5)")
                print()
        category = categories[category_index-1]
        item = input("Enter the item: ")
        while True:
            try:
                amount = float(input("Enter the amount: "))
                if amount <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid positive number")
                print()
        db.addExpense(self.user_name, category, item, amount)

    def getCurrentBudget(self):
        global db
        if (self.isLoggedIn()):
            db.getCurrentBudget(self.user_name)
        else:
            print("You need to log in first.")

    def getCurrentSpending(self):
        global db
        if (self.isLoggedIn()):
            db.getCurrentSpent(self.user_name)
        else:
            print("You need to log in first.")

    def isLoggedIn(self):
        if (self.user_name):
            return True
        return False