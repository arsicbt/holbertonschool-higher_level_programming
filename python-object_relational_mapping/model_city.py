#!/usr/bin/python3
"""
This module defines the City class mapped to the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that inherits from Base and represents the 'cities' table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Add this line to create the relationship with State
    state = relationship("State", backref="cities")
