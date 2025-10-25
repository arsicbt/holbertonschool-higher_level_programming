#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name starts with 'N' (upper N), sorted by id.
"""

import sys
import MySQLdb


def list_states_N():
    """
    Connects to the MySQL database and prints all states
    whose name starts with 'N', ordered by states.id.
    """
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor
    cursor = db.cursor()

    # Execute query to fetch states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", ('N%',))

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_N()
