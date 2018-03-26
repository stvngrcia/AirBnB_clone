#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey=('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
    else:
