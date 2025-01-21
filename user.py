from database import Database

db = Database()  # Global database instance

class User:
    def __init__(self, userName):
        self.user_name = userName

    def __getCategories(self):
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
        return categories[category_index-1]

    def addExpense(self):
        category = self.__getCategories()
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
    
    def reviewAllExpenses(self):
        global db
        if (self.isLoggedIn()):
            data = db.getAllExpenses(self.user_name)
            for expense in data:
                print(f"Item: {expense[0]}, costs: ${expense[1]}.")
        else:
            print("You need to log in first.")

    def reviewExpensesByCategory(self):
        if (self.isLoggedIn()):
            category = self.__getCategories()
            data = db.getExpensesByCategory(self.user_name, category)
            if data:
                for expense in data:
                    print(f"Item: {expense[0]}, costs: ${expense[1]}.")
            else:
                print(f"No expenses found for category: {category}.")
        else:
            print("You need to log in first.")