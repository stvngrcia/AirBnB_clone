#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from models import HBNB_TYPE_STORAGE
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey="states.id", nullable=False)

    else:
        name = ""
        state_id = ""
