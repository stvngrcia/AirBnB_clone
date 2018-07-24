#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    name = ""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all, delete-orphan")
