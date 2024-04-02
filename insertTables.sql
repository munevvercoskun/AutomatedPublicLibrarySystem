-- Inserting dummy data into Users Table
INSERT INTO Users (user_id, username, password, email, full_name, address, phone_number)
VALUES
(1, 'john_doe', 'password123', 'john.doe@email.com', 'John Doe', '123 Main St', '555-1234'),
(2, 'jane_smith', 'pass456', 'jane.smith@email.com', 'Jane Smith', '456 Oak Ave', '555-5678');

-- Inserting dummy data into Books Table
INSERT INTO Books (book_id, title, author, publication_year, genre, ISBN, available_copies, total_copies)
VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction', '978-0-7432-7356-5', 5, 10),
(2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Drama', '978-0-06-112008-4', 3, 8);

-- Inserting dummy data into Reservations Table
INSERT INTO Reservations (reservation_id, user_id, book_id, reservation_date, pickup_date, status)
VALUES
(1, 1, 1, '2024-03-08', '2024-03-10', 'Pending'),
(2, 2, 2, '2024-03-09', '2024-03-12', 'Active');

-- Inserting dummy data into Borrowings Table
INSERT INTO Borrowings (borrowing_id, user_id, book_id, borrow_date, return_date, status)
VALUES
(1, 1, 1, '2024-03-05', '2024-03-15', 'On Loan'),
(2, 2, 2, '2024-03-06', '2024-03-14', 'Returned');

-- Inserting dummy data into Recommendations Table
INSERT INTO Recommendations (recommendation_id, user_id, book_id, recommendation_date)
VALUES
(1, 1, 2, '2024-03-07'),
(2, 2, 1, '2024-03-08');

-- Inserting dummy data into DigitalMedia Table
INSERT INTO DigitalMedia (media_id, title, creator, release_year, type, available_copies, total_copies)
VALUES
(1, 'Introduction to SQL', 'John Smith', 2020, 'e-book', 10, 20),
(2, 'The Art of Programming', 'Jane Doe', 2018, 'audiobook', 8, 15);

-- Inserting dummy data into DigitalBorrowings Table
INSERT INTO DigitalBorrowings (digital_borrowing_id, user_id, media_id, borrow_date, return_date, status)
VALUES
(1, 1, 1, '2024-03-10', '2024-03-20', 'On Loan'),
(2, 2, 2, '2024-03-12', '2024-03-18', 'Returned');

-- Insert data into CDs table
INSERT INTO CDs (cd_id, title, artist, release_year, available_copies, total_copies) VALUES
(1, 'Thriller', 'Michael Jackson', 1982, 5, 10),
(2, 'Back in Black', 'AC/DC', 1980, 3, 8),
(3, 'The Dark Side of the Moon', 'Pink Floyd', 1973, 6, 12);

-- Insert data into DVDs table
INSERT INTO DVDs (dvd_id, title, director, release_year, available_copies, total_copies) VALUES
(1, 'The Godfather', 'Francis Ford Coppola', 1972, 7, 10),
(2, 'The Shawshank Redemption', 'Frank Darabont', 1994, 4, 6),
(3, 'Pulp Fiction', 'Quentin Tarantino', 1994, 6, 8);

-- Insert data into Magazines table
INSERT INTO Magazines (magazine_id, title, publisher, publication_year, available_copies, total_copies) VALUES
(1, 'National Geographic', 'National Geographic Society', 1888, 8, 10),
(2, 'Time', 'Time USA, LLC', 1923, 5, 8),
(3, 'Vogue', 'Condé Nast', 1892, 6, 10);
