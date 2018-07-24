#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.place import place_amenity
from os import getenv


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place",
                                       secondary=place_amenity)
    else:
        name = ""
