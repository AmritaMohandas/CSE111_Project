-- ADMIN CAPABILITIES
-- Add book
INSERT INTO books VALUES(21, 'The Lightning Thief (Percy Jackson and the Olympians #1)', 2006, 'fiction')
-- Add edition
INSERT INTO edition VALUES(21, 49, 9780786838653, 1, 2011)
-- Add author
INSERT INTO author VALUES(21, 'Rick Riordan', 'Alive')
-- Add publisher
INSERT INTO publisher VALUES(49, 'Hyperion')
-- Add user
INSERT INTO users VALUES(21, 'John', 'Doe', 'john.doe@example.com', 'pass123', 'admin')

-- USER CAPABILITIES
-- View collection by title
SELECT b_title, b_firstpublished, b_type
    FROM books
    WHERE b_title = 'Pride and Prejudice'

-- View collection by 1 genre
SELECT DISTINCT(b_title), b_firstpublished, b_type
    FROM books, genres, booksgenres
    WHERE b_bookID = bg_bookID
        AND bg_genreID = g_genreID
        AND g_name = 'Classics'

-- View collection by 2 genre
SELECT DISTINCT(b_title), b_firstpublished, b_type
    FROM books, genres, booksgenres
    WHERE b_bookID = bg_bookID
        AND bg_genreID = g_genreID
        AND g_name = 'Science Fiction'
UNION
SELECT DISTINCT(b_title), b_firstpublished, b_type
    FROM books, genres, booksgenres
    WHERE b_bookID = bg_bookID
        AND bg_genreID = g_genreID
        AND g_name = 'Dystopian'


-- View collection by without certain genres (Science Fiction and Dystopian, but not Young Adult)

-- View collection by author
SELECT DISTINCT(b_title), b_firstpublished, b_type
    FROM books, authors, booksauthors
    WHERE b_bookID = ba_bookID
        AND ba_authorID = a_authorID
        AND a_name = 'Jane Austen'

-- View collection by publisher
SELECT DISTINCT(b_title), b_firstpublished, b_type
    FROM books, publishers, bookspublishers
    WHERE b_bookID = bp_bookID
        AND bp_publisherID = p_publisherID
        AND p_name = 'Penguin Classics'

-- View collection by not deceased authors
SELECT DISTINCT(b_title), b_firstpublished, b_type
    FROM books, authors, booksauthors
    WHERE b_bookID = ba_bookID
        AND ba_authorID = a_authorID
EXCEPT 
SELECT b_title, b_firstpublished, b_type
    FROM books, authors, booksauthors
    WHERE b_bookID = ba_bookID
        AND ba_authorID = a_authorID
        AND a_condition = 'Deceased'
    
-- View collection by 5 star reviews

-- View collection by greatest number of finished reads

-- View collection by format
SELECT DISTINCT(bp_isbn), b_title, p_name
    FROM books, format, bookspublishers, publishers
    WHERE b_bookID = bp_bookID
        AND bp_publisherID = p_publisherID
        AND bp_formatID = f_formatID
        AND f_name = 'Paperback'

-- View books by series
SELECT b_title, b_firstpublished, b_type
    FROM books
    WHERE b_title LIKE '%The Hunger Games%'

-- Add reading status
INSERT INTO readingstatus VALUES(2, 20, 'ToBeRead')

-- Update reading status
UPDATE readingstatus
SET rs_readingstatus = 'CurrentRead', rs_bookID = 2
WHERE user = 20

-- View personal collection based on reading status

-- Add rating and review
INSERT INTO ratings VALUES(12, 1, 20, 5) 
-- Delete rating and review

-- View ratings by rating value

-- View all the genres of a book
-- View all the editions of a book

-- Delete a user
DELETE FROM user
WHERE u_userID = 20
-- Delete a book
DELETE FROM books
WHERE b_bookID = 4

DELETE FROM books
WHERE b_title = 'Emma'

DELETE FROM books
WHERE b_firstpublished = 2017

DELETE FROM books
WHERE b_type = 'fiction'