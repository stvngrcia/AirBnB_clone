#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''

from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", cascade="all, delete-orphan")
        places = relationship("Place", cascade="all, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
