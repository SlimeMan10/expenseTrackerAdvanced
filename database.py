import sqlite3
import hashlib
import secrets
from errors.userNameError import UsernameAlreadyExistsError

class Database:
    def __init__(self):
        self.db_path = 'db/expense_tracker.db'

    def __createConnection(self):
        """Establish a connection to the database."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        return connection, cursor

    def __closeConnection(self, connection, cursor):
        """Safely close the connection and cursor."""
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    def logIn(self, username, password):
        """Authenticate a user."""
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()
            
            # Check if the user exists
            user_record = self.checkUserName(username)
            if not user_record:
                print("Username does not exist.")
                return 1  # Username not found

            # Fetch the stored hash and salt for the user
            password_query = "SELECT hash, salt FROM Users WHERE user_name = ?"
            cursor.execute(password_query, [username])
            result = cursor.fetchone()

            if not result:
                print("Error: Could not retrieve user credentials.")
                return -1  # General error

            stored_hash, stored_salt = result

            # Debugging output
            print(f"Stored hash: {stored_hash}")
            print(f"Stored salt (hex): {stored_salt}")

            # Ensure the salt is in bytes
            if isinstance(stored_salt, str):
                stored_salt = bytes.fromhex(stored_salt)

            # Debugging output
            print(f"Converted salt (bytes): {stored_salt}")

            # Compute the hash of the provided password using the retrieved salt
            computed_hash = self.__hash_password(password, stored_salt)

            # Debugging output
            print(f"Computed hash: {computed_hash}")

            # Compare the computed hash with the stored hash
            if stored_hash == computed_hash:
                print("Login successful.")
                return 0  # Successful login
            else:
                print("Password is incorrect.")
                return 2  # Incorrect password

        except Exception as error:
            print(f"Error logging in: {error}")
            return -1  # General error
        finally:
            self.__closeConnection(connection, cursor)



    def create_new_user(self, username, password):
        """Create a new user."""
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()

            if self.checkUserName(username):
                raise UsernameAlreadyExistsError(f"Username '{username}' is already taken.")

            salt = self.__generate_salt()
            hash = self.__hash_password(password, salt)
            new_user_query = "INSERT INTO Users (user_name, hash, salt) VALUES (?, ?, ?)"
            cursor.execute(new_user_query, [username, hash, salt.hex()])
            connection.commit()
            print(f"User '{username}' created successfully.")
        except Exception as error:
            print(f"Error creating user: {error}")
            if connection:
                connection.rollback()
        finally:
            self.__closeConnection(connection, cursor)

    def checkUserName(self, username):
        #check if user exists in the database
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()
            query = "SELECT 1 FROM Users WHERE user_name = ?"
            cursor.execute(query, [username])
            return cursor.fetchone() is not None
        except Exception as error:
            print(f"Error checking username: {error}")
            return False
        finally:
            self.__closeConnection(connection, cursor)

    def __hash_password(self, password, salt):
        """
        Generate a secure hash of a password using a salt.

        Parameters:
        password (str): The password to be hashed.
        salt (str or bytes): The salt to be used for hashing. If a string is provided, it will be converted to bytes.

        Returns:
        str: The hashed password as a hexadecimal string.
        """
        # Ensure salt is in bytes
        if isinstance(salt, str):
            salt = bytes.fromhex(salt)
        # Combine salt and password securely
        salted_password = salt + password.encode('utf-8')
        # Return the hash as a hexadecimal string
        return hashlib.sha256(salted_password).hexdigest()

    def __generate_salt(self):
        return secrets.token_bytes(16)  # Return salt as bytes
    
    def setBudget(self, username, budget):
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()
            #lets get the current spent to check if the new budget is higher than the current spent
            currentSpend = self.getCurrentSpent(username)
            if budget < currentSpend:
                print("Error: New budget should be higher than the current spent.")
                return
            budgetQuery = "UPDATE Users SET budget = ? WHERE user_name = ?"
            cursor.execute(budgetQuery, [budget, username])
            connection.commit()
            print(f"Budget updated for user '{username}'.")
        except Exception as error:
            print(f"Error updating budget: {error}")
        finally:
            self.__closeConnection(connection, cursor)

    def getCurrentBudget(self, username):
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()
            budgetQuery = "SELECT budget FROM Users WHERE user_name =?"
            cursor.execute(budgetQuery, [username])
            budget = cursor.fetchone()[0]
            print(f"Current budget for user '{username}': ${budget}")
        except Exception as error:
            print(f"Error getting current budget: {error}")
        finally:
            self.__closeConnection(connection, cursor)

    def getCurrentSpent(self, username):
        connection, cursor= None, None
        try:
            connection, cursor = self.__createConnection()
            spendQuery = "SELECT totalSpent FROM Users WHERE user_name =?"
            cursor.execute(spendQuery, [username])
            currentSpend = cursor.fetchone()[0]
            return currentSpend if currentSpend else 0
        except Exception as error:
            print(f"Error getting current spent: {error}")
        finally:
            self.__closeConnection(connection, cursor)
            