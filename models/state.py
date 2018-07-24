#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    name = ""

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all, delete-orphan")
