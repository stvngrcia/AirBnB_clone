#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place',
                                   secondary=place_amenity,
                                   back_populates="amenities")
