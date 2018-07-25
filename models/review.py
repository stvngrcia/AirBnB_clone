#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from models.base_model import BaseModel


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = 'review'
    if (storage_type == 'db'):
        place_id = Column(String(60), nullable=False ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
