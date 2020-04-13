import sqlite3
from sqlite3 import Error

# Create sqlite database
def create_connection(db_file):
    """ Create a sqlite database and test the connection """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r"application/users.db")
    