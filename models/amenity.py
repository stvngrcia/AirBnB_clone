#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey
from models.place import place_amenity

storage_type = getenv('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = 'amenities'
    if (storage_type == 'db'):
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=place_amenity)
    else:
        name = ""
