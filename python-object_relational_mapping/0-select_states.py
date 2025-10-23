#!/bin/env python3
"""
Lists all states of the DB
"""


import sys
import MySQLdb


def list_states():
    """Lists states ordered by id"""
    # Keep arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Conection to DB
    db = MySQLdb.connect(
        host='Localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Cursor to execute requests
    cursor = db.cursor()

    # SQL requests
    cursor.execute("SELECT * FROM states ORDER by id ASC")

    # Keep and display the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
