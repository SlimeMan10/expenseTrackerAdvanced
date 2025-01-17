from user import User

class Admin(User):

    def __init__(self, username):
        super().__init__(username)

    def printCategories(self):
        super().printCategories()
        print("6. Set New Budget")
        print("7. Delete User")
        print("8. Make New Admin")
        print("9. View All Users")
        print("10. Add New Category")
        print("11. View All Spending History")

    def deleteUser(self, username):
        print("WIP - Delete User")
    def makeNewAdmin(self, username):
        print("WIP - Delete User")

    def viewAllUsers(self):
        print("WIP - Delete User")

    #sets a new budget for all users in the database regardless of their current spending
    def capSpending(self, newBudget):
        print("WIP - Delete User")
