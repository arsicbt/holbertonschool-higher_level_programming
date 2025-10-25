#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """Connects to MySQL and deletes States whose name contains 'a'."""
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

    # Query and delete all states with 'a' in the name
    to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in to_delete:
        session.delete(state)

    session.commit()  # save changes
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
