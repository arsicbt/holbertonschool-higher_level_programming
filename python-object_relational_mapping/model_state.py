#!/usr/bin/env python3
"""
Définition du modèle State avec SQLAlchemy
Représente la table 'states' dans la base de données
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création de la classe de base pour tous les modèles
Base = declarative_base()


class State(Base):
    """
    Classe State qui représente la table 'states'
    
    Attributes:
        id (int): Clé primaire auto-incrémentée
        name (str): Nom de l'état (max 128 caractères)
    """
    # Nom de la table dans la base de données
    __tablename__ = 'states'
    
    # Colonnes de la table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
