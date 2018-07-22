#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models import HBNB_TYPE_STORAGE
from sqlalchemy import Column, Integer, String, ForeignKey

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

    else:
        name = ""
