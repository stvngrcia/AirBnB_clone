#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey

storage_type = getenv('HBNB_TYPE_STORAGE')

class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = 'reviews'
    if (storage_type == 'db'):
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
