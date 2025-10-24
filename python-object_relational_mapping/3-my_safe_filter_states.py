#!/usr/bin/python3
""" Safe version, SQL injections friendly """

import sys
import MySQLdb


def safe_version():
    """Connects to a MySQL database and lists all states ordered by id."""
    # Keep arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (searched,))

    # Display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_version()
