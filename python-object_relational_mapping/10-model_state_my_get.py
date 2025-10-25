#!/usr/bin/python3
"""
Prints the State object id with the name passed as argument from the database
hbtn_0e_6_usa.

If a state with the given name exists, prints its id.
If no state is found, prints "Not found".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_id():
    """Connect to the database and print the id of the State matching"""
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Safe query using ORM (prevents SQL injection)
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    get_state_id()
