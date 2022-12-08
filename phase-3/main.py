import sqlite3
from sqlite3 import Cursor, Error

# Sources:
# https://stackoverflow.com/questions/45569344/how-to-tell-if-a-value-exists-in-a-sqlite3-database-python

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

def get_userid(_conn, _u_username):
    try:
        cursor = _conn.cursor()
        
        cursor.execute("""
                        SELECT u_userID
                            FROM users
                            WHERE u_username = ?""", [_u_username])

        row = cursor.fetchall()
        _u_userid = row[0][0]

        return _u_userid

    except Error as e:
        _conn.rollback()
        print(e)


def view_collection(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("View Collection")

    try:
        cursor = _conn.cursor()
        
        cursor.execute("""
                        SELECT b_bookID, b_title, b_firstpublished, b_type
                            FROM books
                        """)

        rows = cursor.fetchall()

        for row in rows:
            tuples = '{}|{}|{}|{}'.format(row[0], row[1], row[2], row[3])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_collection_by_bookid(_conn, _bookid):
    print("++++++++++++++++++++++++++++++++++")

    try:
        cursor = _conn.cursor()

        cursor.execute("""
                        SELECT b_title, b_firstpublished, b_type
                            FROM books
                            WHERE b_bookID = ?""", [_bookid])

        rows = cursor.fetchall()

        for row in rows:
            tuples = '{}|{}|{}'.format(row[0], row[1], row[2])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_collection_by_title(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("View Collection by Title")
    try:
        _title = input()
        cursor = _conn.cursor()
        query = "SELECT b_bookID, b_title, b_firstpublished, b_type " + \
                     "FROM books " + \
                     "WHERE b_title LIKE " + \
                     "'%" + _title + "%'"

        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            tuples = '{}|{}|{}|{}'.format(row[0], row[1], row[2], row[3])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_collection_by_author(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("View Collection by Author")
    try:
        _authorname = input()
        cursor = _conn.cursor()
        query = "SELECT b_bookID, b_title, b_firstpublished, b_type " + \
                     "FROM books, authors, booksauthors " + \
                     "WHERE b_bookID = ba_bookID " + \
                     "AND ba_authorID = a_authorID " + \
                     "AND a_name LIKE " + \
                     "'%" + _authorname + "%'"

        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            tuples = '{}|{}|{}|{}'.format(row[0], row[1], row[2], row[3])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_collection_by_genre(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("View Collection by Genre")
    try:
        _genrename = input()
        cursor = _conn.cursor()
        query = "SELECT b_bookID, b_title, b_firstpublished, b_type " + \
                     "FROM books, genres, booksgenres " + \
                     "WHERE b_bookID = bg_bookID " + \
                     "AND bg_genreID = g_genreID " + \
                     "AND g_name LIKE " + \
                     "'%" + _genrename + "%'"

        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            tuples = '{}|{}|{}|{}'.format(row[0], row[1], row[2], row[3])
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def view_reading_list(_conn, _u_username):
    print("++++++++++++++++++++++++++++++++++")
    print("Reading List:")

    try:
        cursor = _conn.cursor()
        cursor.execute("""SELECT b_bookID, b_title, b_firstpublished, b_type
                        FROM books, users, readingstatus
                        WHERE b_bookID = rs_bookID
                            AND rs_userID = u_userID
                            AND u_username = ?""", [_u_username])
        rows = cursor.fetchall()
        count = 1
        for row in rows:
            tuples = '{}|{}|{}|{}'.format(row[0], row[1], row[2], row[3])
            count += 1
            print(tuples + '\n')

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def view_author_of_book(_conn, _bookid):
    print("++++++++++++++++++++++++++++++++++")
    print("Author(s):")

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
    print("Genre(s):")

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
    print("Edition(s):")

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

def user_login(_conn):
    # Create cursor object
    cursor = _conn.cursor()

    _authenticated = False
    _u_username = ""
    _u_username = input("Username: ")
    _u_password = input("Password: ")

    cursor.execute("""SELECT u_username
                        FROM users
                        WHERE u_username=?
                            AND u_password=?""",[_u_username, _u_password])

    result = cursor.fetchone()

    if result:
        _authenticated, _u_username = result, _u_username
    else:
        print("Username or password is incorrect. Enter again: ")
    
    return _authenticated, _u_username

def create_new_account(_conn):
    # Create cursor object
    cursor = _conn.cursor()

    _u_firstname = input("First Name: ")
    _u_lastname = input("Last Name: ")
    _u_username = input("Username: ")
    _u_email = input("Email: ")
    _u_password = input("Password: ")
    _u_category = "user"

    cursor.execute("""SELECT u_username
                        FROM users
                        WHERE u_username=?
                            AND u_email=?""",[_u_username, _u_email])

    result = cursor.fetchone()

    if result:
        print("This user already exists. Select a new username and/or email:")
        create_new_account(_conn)
    else:
        cursor.execute("""INSERT INTO users (u_firstname, u_lastname, u_username, u_email, u_password, u_category) VALUES (?, ?, ?, ?, ?, ?)""", 
                                        (_u_firstname, _u_lastname, _u_username, _u_email, _u_password, _u_category))
        _conn.commit()

def display_menu(_conn, _u_username):
    exit = True
    while exit == True:
        print("S. Search, R. Reading list, L. Logout")
        userInput = input()
        if userInput == "S":
            print("Search by - T. Title, A. Author, G. Genre:")
            userInput = input()
            if userInput == "T":
                view_collection_by_title(_conn)
                print("To view a specific book, select the number, M. Menu")
                _bookid = input()
                if _bookid != "M":
                    view_book_info(_conn, _bookid, _u_username)
                elif _bookid == "M":
                    # display_menu(_conn, _u_username)
                    continue
            elif userInput == "A":
                view_collection_by_author(_conn)
                print("To view a specific book, select the number, M. Menu")
                _bookid = input()
                if _bookid != "M":
                    view_book_info(_conn, _bookid, _u_username)
                elif _bookid == "M":
                    # display_menu(_conn, _u_username)
                    continue
            elif userInput == "G":
                view_collection_by_genre(_conn)
                print("To view a specific book, select the number, M. Menu")
                _bookid = input()
                if _bookid != "M":
                    view_book_info(_conn, _bookid, _u_username)
                elif _bookid == "M":
                    # display_menu(_conn, _u_username)
                    continue
        elif userInput == "R":
            view_reading_list(_conn, _u_username)
            print("To view a specific book, select the number, M. Menu")
            _bookid = input()
            if _bookid != "M":
                view_book_info(_conn, _bookid, _u_username)
            elif _bookid == "M":
                # display_menu(_conn, _u_username)
                continue
        elif userInput == "L":
            exit = False

def view_book_info(_conn, _bookid, _u_username):
    back = True
    while back == True:
        view_collection_by_bookid(_conn, _bookid)
        print("1. Author", "2. Genre", "3. Edition", "4. Reading Status", "5. Back", "6. Delete from Reading List")
        userInput = input()
        if userInput == "1":
            view_author_of_book(_conn, _bookid)
        elif userInput == "2":
            view_genre_of_book(_conn, _bookid)
        elif userInput == "3":
            view_edition_of_book(_conn, _bookid)
        elif userInput == "4":
            view_reading_status(_conn, _bookid, _u_username)
        elif userInput == "5":
            back = False
        elif userInput == "6":
            print("Deleted from Reading List")
            delete_from_readinglist(_conn, _bookid, _u_username)
            back = False

def view_reading_status(_conn, _bookid, _u_username):
    cursor = _conn.cursor()
    
    back = True
    cursor.execute("""SELECT rs_readStatus
                        FROM books, users, readingstatus
                        WHERE b_bookID = rs_bookID
                            AND rs_userID = u_userID
                            AND u_username = ?
                            AND b_bookID = ?""", [_u_username, _bookid])

    result = cursor.fetchone()

    if result:
        while back == True:
            print("U. Update Reading Status, B. Back")
            _rs_readStatus = '{}'.format(result[0])
            print(_rs_readStatus + '\n')
            userInput = input()
            if userInput == "U":
                _rs_readStatus = update_reading_status(_conn, _bookid, _u_username)
            elif userInput == "B":
                back = False
    else:
        print("A. Add Reading Status, B. Back")
        print("No Reading Status")
        userInput = input()
        if userInput == "A":
            _rs_readStatus = insert_reading_status(_conn, _bookid, _u_username)
        elif userInput == "B":
            back = False

def delete_from_readinglist(_conn, _bookid, _u_username):
    cursor = _conn.cursor()
    _u_userid = get_userid(_conn, _u_username)
    cursor.execute("""DELETE FROM readingstatus WHERE rs_bookID = ? AND rs_userID = ?""", [_bookid, _u_userid])
    _conn.commit()       

def update_reading_status(_conn, _bookid, _u_username):
    cursor = _conn.cursor()
    _rs_readStatus = ""
    _rs_readStatus = select_reading_status(_rs_readStatus)
    _u_userid = get_userid(_conn, _u_username)
    cursor.execute("""UPDATE readingstatus SET rs_readStatus = ? WHERE rs_bookID = ? AND rs_userID = ?""", [_rs_readStatus, _bookid, _u_userid])
    _conn.commit()

    return _rs_readStatus

def insert_reading_status(_conn, _bookid, _u_username):
    cursor = _conn.cursor()
    _rs_readStatus = ""
    _rs_readStatus = select_reading_status(_rs_readStatus)
    _u_userid = get_userid(_conn, _u_username)
    cursor.execute("""INSERT INTO readingstatus (rs_bookID, rs_userID, rs_readStatus) VALUES (?, ?, ?)""", [_bookid, _u_userid, _rs_readStatus])
    _conn.commit()

    return _rs_readStatus
    
def select_reading_status(_rs_readStatus):
    print("1. ToBeRead, 2. FinishedRead, 3. CurrentRead, 4. DidNotFinish")
    userInput = input()
    if userInput == "1":
        _rs_readStatus = "ToBeRead"
    elif userInput == "2":
        _rs_readStatus = "FinishedRead"
    elif userInput == "3":
        _rs_readStatus = "CurrentRead"
    elif userInput == "4":
        _rs_readStatus = "DidNotFinish"
    return _rs_readStatus


def main():
    database = r"db.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:

        print("LOGIN MENU")
        print("-----------")
        print("1. New User")
        print("2. User Login")
        print("------------")
        _authenticated = False
        _u_username = ""
        userInput = int(input())
        if userInput == 1:
            print("USER REGISTRATION")
            print("-------------------")
            create_new_account(conn)
            print("-------------------------")
            print("Successfully Registered")
        elif userInput == 2:
            while _authenticated == False:
                _authenticated, _u_username = user_login(conn)
            display_menu(conn, _u_username)
            print("-------------------------")
            print("Successfully Logged Out")

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
