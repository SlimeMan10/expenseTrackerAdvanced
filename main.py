from connection import Connection

# Constants
totalChoices = 8
connection = Connection()

# Entry Point
def init():
    print("Expense Tracker")
    print("1. Log In")
    print("2. Sign Up")
    print("0. Log Out")
    verifyIntroduction()

def verifyIntroduction():
    while True:
        try:
            num = int(input("Option: "))
            if num < 0 or num > 2:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number (0, 1, 2)")
            print()
    if num == 1:
        logIn()
    elif num == 2:
        signUp()
    else:
        print("Exiting the application.")
        exit()

def logIn():
    global connection
    loggedIn = connection.logIn()
    if loggedIn:
        connection.start()
    else:
        init()

def signUp():
    global connection
    loggedIn = connection.signUp()
    if loggedIn:
        connection.start()
    else:
        init()

# Graceful exit for keyboard interrupt
try:
    init()
except KeyboardInterrupt:
    print("\nconnectioner exited. Goodbye!")