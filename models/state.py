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
        @property
        def cities (self):
        '''
        Getter for citites
        '''
        all_cities = models.storage.all(City)
        cities = {}
        for key, obj in city_list:
            if key == state_id:
                cities[key] = obj
        return cities

    def __init__(self):
        '''
        Instantiate State
        '''
        super().__init__()
