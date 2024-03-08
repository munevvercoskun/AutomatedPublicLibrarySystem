-- Users Table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255),
    full_name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(20)
);

-- Books Table
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    publication_year INT,
    genre VARCHAR(255),
    ISBN VARCHAR(20),
    available_copies INT,
    total_copies INT
);

-- Reservations Table
CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    reservation_date DATE,
    pickup_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Borrowings Table
CREATE TABLE Borrowings (
    borrowing_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Recommendations Table
CREATE TABLE Recommendations (
    recommendation_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    recommendation_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Digital Media Table
CREATE TABLE DigitalMedia (
    media_id INT PRIMARY KEY,
    title VARCHAR(255),
    creator VARCHAR(255),
    release_year INT,
    type VARCHAR(50),
    available_copies INT,
    total_copies INT
);

-- Digital Borrowings Table
CREATE TABLE DigitalBorrowings (
    digital_borrowing_id INT PRIMARY KEY,
    user_id INT,
    media_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (media_id) REFERENCES DigitalMedia(media_id)
);
