import sqlite3
from sqlite3 import Cursor, Error

# for function view_collection_by_inputWord(_conn, _inputWord)
    # takes in string from user (either a book title, author, or genre)
    # function should display the books that are associated with the user input string

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def view_collection(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("View Collection")

    try:
        cursor = _conn.cursor()
        cursor.execute("""
                        SELECT b_title, b_firstpublished, b_type
                            FROM books
                        """)
        rows = cursor.fetchall()
        count = 1
        for row in rows:
            tuples = '{}|{}|{}|{}'.format(count, row[0], row[1], row[2])
            count += 1
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

# def view_collection_by_author(_conn, _authorname):
#     print("++++++++++++++++++++++++++++++++++")
#     print("View Collection by Author")
#     try:
#         cursor = _conn.cursor()
#         query = "SELECT b_title, b_firstpublished, b_type " + \
#                      "FROM books, authors, booksauthors " + \
#                      "WHERE b_bookID = ba_bookID " + \
#                      "AND ba_authorID = a_authorID " + \
#                      "AND a_name LIKE " + \
#                      "'%" + _authorname + "%'"

#         cursor.execute(query)
#         rows = cursor.fetchall()
#         count = 1
#         for row in rows:
#             tuples = '{}|{}|{}|{}'.format(count, row[0], row[1], row[2])
#             count += 1
#             print(tuples + '\n')

#     except Error as e:
#         _conn.rollback()
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")

def view_collection_by_inputWord(_conn, _inputWord): 
    print("++++++++++++++++++++++++++++++++++")
    print("View Collection by Input")
    try:
        cursor = _conn.cursor()
        query = "SELECT distinct(b_title), b_firstpublished, b_type " + \
                     "FROM books, authors, genres, booksauthors, booksgenres " + \
                     "WHERE b_bookID = ba_bookID " + \
                     "AND ba_authorID = a_authorID " + \
                     "AND b_bookID = bg_bookID " + \
                     "AND bg_genreID = g_genreID " + \
                     "AND a_name LIKE " + \
                     "'%" + _inputWord + "%'" + \
                     "OR g_name LIKE " + \
                     "'%" + _inputWord + "%'"

        cursor.execute(query)
        rows = cursor.fetchall()
        count = 1
        for row in rows:
            tuples = '{}|{}|{}|{}'.format(count, row[0], row[1], row[2])
            count += 1
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_author_of_book(_conn, _bookid):
    print("++++++++++++++++++++++++++++++++++")
    print("View Author of Book")

    try:
        cursor = _conn.cursor()
        cursor.execute("""
                        SELECT a_name
                            FROM books, authors, booksauthors
                            WHERE b_bookID = ba_bookID
                                AND ba_authorID = a_authorID
                                AND b_bookID = ?""",[_bookid])
        rows = cursor.fetchall()
        for row in rows:
            tuples = '{}'.format(row[0])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_genre_of_book(_conn, _bookid):
    print("++++++++++++++++++++++++++++++++++")
    print("View Genre of Book")

    try:
        cursor = _conn.cursor()
        cursor.execute("""
                        SELECT g_name
                            FROM books, genres, booksgenres
                            WHERE b_bookID = bg_bookID
                                AND bg_genreID = g_genreID
                                AND b_bookID = ?""",[_bookid])
        rows = cursor.fetchall()
        for row in rows:
            tuples = '{}'.format(row[0])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_edition_of_book(_conn, _bookid):
    print("++++++++++++++++++++++++++++++++++")
    print("View Edition of Book")

    try:
        cursor = _conn.cursor()
        cursor.execute("""
                        SELECT p_name, bp_isbn, f_name, bp_publishyear
                            FROM books, publishers, format, bookspublishers
                            WHERE b_bookID = bp_bookID
                                AND f_formatID = bp_formatID
                                AND bp_publisherID = p_publisherID
                                AND b_bookID = ?""",[_bookid])
        rows = cursor.fetchall()
        for row in rows:
            tuples = '{}|{}|{}|{}'.format(row[0], row[1], row[2], row[3])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def user_login(_conn, _u_username, _u_password):
    # Create cursor object
    cursor = _conn.cursor()

    # run a select query against the table to see if any record exists
    # that has the email or username
    cursor.execute("""SELECT u_username
                   FROM users
                   WHERE u_username=?
                       AND u_password=?""",[_u_username, _u_password])

    # Fetch one result from the query because it
    # doesn't matter how many records are returned.
    # If it returns just one result, then you know
    # that a record already exists in the table.
    # If no results are pulled from the query, then
    # fetchone will return None.
    result = cursor.fetchone()

    if result:
        # Record already exists
        # Do something that tells the user that email/user handle already exists
        return True

def create_new_account(_conn, _u_firstname, _u_lastname, _u_username, _u_email, _u_password, _u_category):
    # Create cursor object
    cursor = _conn.cursor()

    # https://stackoverflow.com/questions/45569344/how-to-tell-if-a-value-exists-in-a-sqlite3-database-python
    # run a select query against the table to see if any record exists
    # that has the email or username
    cursor.execute("""SELECT u_username
                        FROM users
                        WHERE u_username=?
                            AND _u_email=?""",[_u_username, _u_email])

    # Fetch one result from the query because it
    # doesn't matter how many records are returned.
    # If it returns just one result, then you know
    # that a record already exists in the table.
    # If no results are pulled from the query, then
    # fetchone will return None.
    result = cursor.fetchone()

    if result:
        # Record already exists
        # Do something that tells the user that email/user handle already exists
        return False
    else:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (_u_firstname, _u_lastname, _u_username, _u_email, _u_password, _u_category))
        

def main():
    database = r"db.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:

        # print("1. Author", "2. Genre", "3. Edition")
        # _bookid = 9
        # userInput = input()
        # if userInput == "1":
        #     view_author_of_book(conn, _bookid)
        # elif userInput == "2":
        #     view_genre_of_book(conn, _bookid)
        # elif userInput == "3":
        #     view_edition_of_book(conn, _bookid)
        
        # print("1. Search by title/author/genre")
        # view_collection(conn)
        # _inputWord = input()
        # view_collection_by_inputWord(conn, _inputWord)
        # view_collection_by_title(conn, _titlename)
        # view_collection_by_genre(conn)

        print("Select one of the following:")
        print("1. New User, 2. Login")
        _u_userID = input()
        _u_firstname = input()
        _u_lastname = input()
        _u_username = input()
        _u_email = input()
        _u_password = input()
        _u_category = input()
        create_new_account(conn, _u_userID, _u_firstname, _u_lastname,	_u_username, _u_email, _u_password, _u_category)

        # _u_username = input()
        # _u_password = input()
        # check = user_login(conn, _u_username, _u_password)


    closeConnection(conn, database)


if __name__ == '__main__':
    main()
