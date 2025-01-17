import sqlite3

# Path to your database
db_path = 'db/expense_tracker.db'

def get_all_users():
    """Fetch all users from the Users table."""
    connection = None
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Query to fetch all users
        query = "SELECT * FROM Users"
        cursor.execute(query)
        result = cursor.fetchall()

        # Check if there are any users
        if result:
            users = [row[0] for row in result]
            print("Users in the database:", users)
            return users
        else:
            print("No users found in the database.")
            return []

    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

    finally:
        if connection:
            connection.close()

# Fetch and print all users
get_all_users()