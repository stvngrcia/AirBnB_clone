#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    name = ""
