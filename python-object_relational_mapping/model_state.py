#!/usr/bin/python3
"""
Module qui liste tous les états en utilisant SQLAlchemy ORM
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states():
    """Liste tous les états triés par id en utilisant SQLAlchemy"""
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Création de la connexion à la base de données
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Création d'une session pour interagir avec la base
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Requête ORM (équivalent de: SELECT * FROM states ORDER BY id ASC)
    states = session.query(State).order_by(State.id).all()
    
    # Affichage des résultats
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Fermeture de la session
    session.close()


if __name__ == "__main__":
    list_states()
