#!/usr/bin/python3
'''
    Implementation of the State class
'''

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

storage_type = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    if (storage_type == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        name = ""
        @property
        def get_cities(self):
            city_list = []
            for val in storage.all(City).values():
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
