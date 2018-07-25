#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

storage_type = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = 'users'
    if (storage_type == 'db'):
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete-orphan", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
