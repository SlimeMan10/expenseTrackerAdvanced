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
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()
            
            # Check if the user exists
            if not self.checkUserName(username):
                print("Username does not exist.")
                return 1  # Username not found

            # Fetch the stored hash and salt for the user
            password_query = "SELECT hash, salt FROM Users WHERE user_name = ?"
            cursor.execute(password_query, [username])
            result = cursor.fetchone()

            if result is None:
                print("Error: User record could not be retrieved.")
                return 1  # Username not found

            stored_hash, stored_salt = result

            # Ensure salt is in bytes
            if isinstance(stored_salt, str):
                stored_salt = bytes.fromhex(stored_salt)

            # Compute the hash of the provided password
            computed_hash = self.__hash_password(password, stored_salt)

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

            if not self.checkUserName(username):
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
        """Check if a username is already taken."""
        connection, cursor = None, None
        try:
            connection, cursor = self.__createConnection()
            query = "SELECT 1 FROM Users WHERE user_name = ?"
            cursor.execute(query, [username])
            return cursor.fetchone() is None
        except Exception as error:
            print(f"Error checking username: {error}")
            return False
        finally:
            self.__closeConnection(connection, cursor)

    def __hash_password(self, password, salt):
        """Hash the password using SHA-256 with a salt."""
        # Ensure salt is in bytes
        if isinstance(salt, str):
            salt = bytes.fromhex(salt)
        salted_password = salt + password.encode('utf-8')
        return hashlib.sha256(salted_password).hexdigest()

    def __generate_salt(self):
        """Generate a random 16-byte salt."""
        return secrets.token_bytes(16)  # Return salt as bytes