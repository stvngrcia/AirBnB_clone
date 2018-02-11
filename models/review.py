#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Implementation for the Review.
    '''
    place_id = ""
    user_id = ""
    text = ""
