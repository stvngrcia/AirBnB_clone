#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
import os 
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"

    name = ""
    state_id = ""

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
