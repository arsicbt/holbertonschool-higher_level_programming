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
    c = db.cursor()

    # Execute query to fetch states starting with 'N'
    c.execute("SELECT * FROM states WHERE BINARY name\
                LIKE 'N%' ORDER BY id ASC")

    # Fetch and display results
    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    c.close()
    db.close()


if __name__ == "__main__":
    list_states_N()
