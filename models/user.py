#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
        Definition of the User class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
