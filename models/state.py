#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import city
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    def __init__(self):
        '''
        Instantiate State
        '''
        super().__init__()

"""
    if getenv('HBNB_TYPE_STORAGE') is not 'db':
        @property
        def cities(self):
            '''
            Set getter for cities
            '''
            all_cities = models.storage.all(city)
            for 
"""
