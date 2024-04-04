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

-- Borrowings Table
CREATE TABLE Borrowings (
    borrowing_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    returned BOOLEAN=True,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- CDs Table
CREATE TABLE CDs (
    cd_id INT PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    release_year INT,
    available_copies INT,
    total_copies INT
);

-- DVDs Table
CREATE TABLE DVDs (
    dvd_id INT PRIMARY KEY,
    title VARCHAR(255),
    director VARCHAR(255),
    release_year INT,
    available_copies INT,
    total_copies INT
);

-- Magazines Table
CREATE TABLE Magazines (
    magazine_id INT PRIMARY KEY,
    title VARCHAR(255),
    publisher VARCHAR(255),
    publication_year INT,
    available_copies INT,
    total_copies INT
);

-- BorrowedCDs Table
CREATE TABLE BorrowedCDs (
    borrow_id INT PRIMARY KEY,
    user_id INT,
    cd_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (cd_id) REFERENCES CDs(cd_id)
);

-- BorrowedDVDs Table
CREATE TABLE BorrowedDVDs (
    borrow_id INT PRIMARY KEY,
    user_id INT,
    dvd_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (dvd_id) REFERENCES DVDs(dvd_id)
);

-- BorrowedMagazines Table
CREATE TABLE BorrowedMagazines (
    borrow_id INT PRIMARY KEY,
    user_id INT,
    magazine_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (magazine_id) REFERENCES Magazines(magazine_id)
);
CREATE TABLE BorrowedItems (
    borrow_id INT PRIMARY KEY,
    user_id INT,
    item_id INT,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    -- Add foreign key references to other item tables such as Books, CDs, DVDs, etc.
);
CREATE TABLE CartItems (
    cart_id INT PRIMARY KEY,
    user_id INT,
    item_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    -- Add foreign key references to other item tables such as Books, CDs, DVDs, etc.
);
