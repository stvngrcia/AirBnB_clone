#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
