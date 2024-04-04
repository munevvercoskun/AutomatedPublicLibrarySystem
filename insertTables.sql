-- Insert dummy data into Users table
INSERT INTO Users (user_id, username, password, email, full_name, address, phone_number) 
VALUES
(1, 'john_doe', 'password123', 'john.doe@example.com', 'John Doe', '123 Main St', '555-1234'),
(2, 'jane_smith', 'pass456', 'jane.smith@example.com', 'Jane Smith', '456 Oak Ave', '555-5678');

-- Insert dummy data into Items table for books
INSERT INTO Items (item_id, title, type, available)
VALUES
(1, 'To Kill a Mockingbird', 'book', 1),
(2, '1984', 'book', 1);

-- Insert dummy data into Items table for CDs
INSERT INTO Items (item_id, title, type, available)
VALUES
(3, 'Thriller', 'cd', 1),
(4, 'The Dark Side of the Moon', 'cd', 1);

-- Insert dummy data into Items table for DVDs
INSERT INTO Items (item_id, title, type, available)
VALUES
(5, 'The Godfather', 'dvd', 1),
(6, 'Pulp Fiction', 'dvd', 1);

-- Insert dummy data into Items table for Magazines
INSERT INTO Items (item_id, title, type, available)
VALUES
(7, 'National Geographic', 'magazine', 1),
(8, 'Time', 'magazine', 1);
