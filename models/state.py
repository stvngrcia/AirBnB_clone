#!/usr/bin/python3
'''
    Defines the class State.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    '''
        Defines the class State that inherits from BaseModel and Base, the
        declarative base from SQLAlchemy.

        State objects will be mapped to a MySQL table called 'states'

        Since State objects inherit from BaseModel, they will have access to
        the following Columns:
            `BaseModel.id`
            `BaseModel.created_at`
            `BaseModel.updated_at`
    '''

    if os.getenv('HBNB_STORAGE_TYPE') == 'file':

        @property
        def cities(self):
            '''Getter method that returns the list of City instances for
            FileStorage engine.'''
            city_list = []
            for city in self.cities:
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list

    else:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
