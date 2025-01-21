from user import User

class Admin(User):

    def __init__(self, username):
        super().__init__(username)

    def deleteUser(self, username):
        print("WIP - Delete User")
    def makeNewAdmin(self, username):
        print("WIP - Delete User")

    def viewAllUsers(self):
        print("WIP - Delete User")

    #sets a new budget for all users in the database regardless of their current spending
    def capSpending(self, newBudget):
        print("WIP - Delete User")
