from connection import Connection

# Constants
totalChoices = 8
connection = Connection()

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
    global connection
    connection.logIn()
    connection.start()

def signUp():
    global connection
    connection.signUp()
    connection.start()

# Graceful exit for keyboard interrupt
try:
    init()
except KeyboardInterrupt:
    print("\nconnectioner exited. Goodbye!")