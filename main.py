from backendMain import Tracker as tracker

# Constants
totalChoices = 8
track = tracker()  # Global tracker track

# Entry Point
def init():
    print("Expense Tracker")
    print("1. Log In")
    print("2. Sign Up")
    verifyIntroduction()

def verifyIntroduction():
    while True:
        try:
            num = int(input("Option: "))
            if num < 1 or num > 2:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number (1 or 2)")
            print()
    if num == 1:
        logIn()
    else:
        signUp()

def logIn():
    global track
    track.logIn()
    start()

def signUp():
    global track
    track.signUp()
    startNewBudget()

def startNewBudget():
    global track
    print("Starting new budget")
    while True:
        try:
            num = int(input("Enter your budget (must be greater than zero): "))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid positive number")
    start()

def start():
    while True:
        printOptions()
        try:
            choice = int(input("Choice: "))
            if choice < 0 or choice > totalChoices:
                raise ValueError
        except ValueError:
            print("Enter a valid choice")
            print()
            continue
        if choice == 0:
            print("Exiting the tracker. Goodbye!")
            break
        checkOptions(choice)

def checkOptions(choice):
    if choice == 1:
        addExpense()
    elif choice == 2:
        removeExpense()
    elif choice == 3:
        reviewAll()
    elif choice == 4:
        reviewCategory()
    elif choice == 5:
        save()
    elif choice == 6:
        updateBudget()
    elif choice == 7:
        printBudget()
    elif choice == 8:
        getRemainingBudget()

def printBudget():
    global track
    track.getCurrentBudget()

def getRemainingBudget():
    global track
    print(track.getRemainingBudget())

def addExpense():
    global track
    category = getCategory()
    name = input("What is the name of the expense? ")
    while True:
        try:
            price = float(input("What is the price of the expense? "))
            if price < 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid price")
    track.add_expense(category, name, price)
    print(f"Added '{name}' (${price}) to category '{category}'.")

def removeExpense():
    global track
    category = getCategory()
    track.printCategory(category)
    size = track.sizeOfCategory(category)
    if (size == 0):
        print("Category is empty")
    else:
        while True:
            try:
                index = int(input("Enter the number of the item to remove: "))
                if index < 1 or index > size:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid number")
        track.remove_expense(category, index-1)
        print("Expense removed successfully.")

def reviewAll():
    global track
    track.printAll()

def reviewCategory():
    global track
    category = getCategory()
    track.printCategory(category)

def getCategory():
    while True:
        try:
            printCategories()
            item = int(input("Choose a category (1-6) or 0 to cancel: "))
            if item < 1 or item > 6:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number between 1 and 6")
    if item == 1:
        return "food"
    elif item == 2:
        return "transport"
    elif item == 3:
        return "shopping"
    elif item == 4:
        return "entertainment"
    elif item == 5:
        return "travel"
    elif item == 6:
        return "technology"

def printCategories():
    print("1. Food")
    print("2. Transport")
    print("3. Shopping")
    print("4. Entertainment")
    print("5. Travel")
    print("6. Technology")

#TODO
def save():
    global track
    name = input("What will your file name be: ")
    track.save(name)

def updateBudget():
    global track
    while True:
        try:
            num = float(input("Enter your new budget (must be greater than zero): "))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid positive number")
    track.setNewBudget(num)
    print(f"New budget set to ${num:.2f}")

def printOptions():
    print("Here are your options:")
    print("1. Add purchase")
    print("2. Remove purchase")
    print("3. Review all purchases")
    print("4. Review a specific category")
    print("5. Save current tracker")
    print("6. Change budget")
    print("7. View current budget")
    print("8. View remaining budget")
    print("0. Exit")

# Graceful exit for keyboard interrupt
try:
    init()
except KeyboardInterrupt:
    print("\nTracker exited. Goodbye!")