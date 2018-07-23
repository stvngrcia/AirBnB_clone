#!/usr/bin/python3
'''
    Implementation of the State class
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    city = relationship('City', backref='state')

    @property
    def cities(self):
        """
        Returns list of City instances with specific state id
        """
        city_inst = models.storage.all('City').values()
        all_cities = [inst for inst in city_inst if inst.state_id == self.id]
        return all_cities
