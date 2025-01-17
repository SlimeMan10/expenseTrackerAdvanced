CREATE TABLE Roles (
    role_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Users (
    user_name VARCHAR(255) PRIMARY KEY,
    role_name VARCHAR(255) DEFAULT 'user',
    hash BLOB NOT NULL,
    salt BLOB NOT NULL,
    FOREIGN KEY (role_name) REFERENCES Roles(role_name) ON DELETE CASCADE
);

CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL,
    user_name VARCHAR(255),
    is_custom BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE
);

CREATE TABLE Items (
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INTEGER NOT NULL,
    user_name VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE,
    FOREIGN KEY (user_name) REFERENCES Users(user_name) ON DELETE CASCADE
);