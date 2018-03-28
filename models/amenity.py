#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from models.place import place_amenity
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')
