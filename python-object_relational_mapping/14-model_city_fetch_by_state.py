#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa,
sorted by cities.id in ascending order.

Format: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state():
    """Connects to MySQL and prints cities grouped by state."""
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

    # Query all cities, joined with their states, ordered by city id
    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
