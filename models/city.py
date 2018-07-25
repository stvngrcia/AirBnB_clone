#!/usr/bin/python3
'''
    Define the class City.
'''

from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey

storage_type = getenv('HBNB_TYPE_STORAGE')

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    if (storage_type == 'db'):
        name = Column(
            String(128),
            nullable=False
        )
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", cascade="all, delete-orphan", backref="cities")
    else:
        name = ""
