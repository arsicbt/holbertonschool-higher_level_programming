#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
and prints the new state's id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana():
    """Connects to MySQL, adds 'Louisiana' State, and prints its id."""
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()  # commit to save to DB

    # Print new state's id
    print(new_state.id)

    # Close session
    session.close()


if __name__ == "__main__":
    add_louisiana()
