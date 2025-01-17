-- Create Roles table
CREATE TABLE Roles (
    role_name VARCHAR(255) PRIMARY KEY
);

-- Create Users table
CREATE TABLE Users (
    user_name VARCHAR(255) PRIMARY KEY,
    role_name VARCHAR(255) DEFAULT 'user',
    hash BLOB NOT NULL,
    salt BLOB NOT NULL,
    budget NUMBER DEFAULT 1000,
    totalSpent NUMBER DEFAULT 0,
    FOREIGN KEY (role_name) REFERENCES Roles(role_name) ON DELETE CASCADE
);

-- Create Categories table
CREATE TABLE Categories (
    category_name VARCHAR(255) PRIMARY KEY,
    user_name VARCHAR(255) DEFAULT NULL, /* When the admin creates one for all, it will default to NULL */
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE
);

-- Create Items table
CREATE TABLE Items (
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_name INTEGER NOT NULL,
    user_name VARCHAR(255),
    FOREIGN KEY (category_name) REFERENCES Categories(category_name) ON DELETE CASCADE,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE
);