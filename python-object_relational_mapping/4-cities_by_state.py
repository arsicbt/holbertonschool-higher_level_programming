#!/usr/bin/python3
""" Lists cities from DB """

import sys
import MySQLdb


def list_cities():
    """Connects to a MySQL database and lists all states ordered by id."""
    # Keep arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connection to DB
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Cursor to execute queries
    cursor = db.cursor()

    # SQL query
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    # Display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
