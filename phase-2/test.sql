-- ADMIN CAPABILITIES
-- Add book
    -- INSERT INTO books VALUES(21, 'The Lightning Thief (Percy Jackson and the Olympians #1)', 2006, 'fiction')

-- Add edition

-- Add author
-- Add user
-- Add publisher
-- Delete a user

-- USER CAPABILITIES
-- View collection by title
SELECT b_title, b_firstpublished, b_type
    FROM books
    WHERE b_title = 'Pride and Prejudice'

-- View collection by genre
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


-- View books by series
SELECT b_title, b_firstpublished, b_type
    FROM books
    WHERE b_title LIKE '%The Hunger Games%'

-- Add reading status
-- Update reading status
-- View personal collection based on reading status
-- Add rating and review
-- Delete rating and review
-- View ratings by rating value

-- View all the genres of a book
-- View all the editions of a book