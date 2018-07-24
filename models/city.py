#!/usr/bin/python3
'''
    Define the class City.
'''
import models
from models.base_model import BaseModel, Base
from models.place import Place
from os import getenv 
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship(Place, backref="cities", cascade="all, delete-orphan")

    else:
        name = ""
        state_id = ""
