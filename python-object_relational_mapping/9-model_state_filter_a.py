#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a():
    """Connects to MySQL and prints State objects containing 'a'"""
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a configured session
    Session = sessionmaker(bind=engine)
    s = Session()

    # Query states containing 'a', ordered by id
    st = s.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in st:
        print(f"{state.id}: {state.name}")

    # Close session
    s.close()


if __name__ == "__main__":
    list_states_with_a()
