#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
import datetime


class BaseModel:
    '''
        Base class for other classes to be used for the duration
        of this project.
    '''
    def __init__(self):
        '''
            Initialize public instance attributes.
            Attributes:
                id: id of an instance
                created_at: Time of instance creation
                updated_at: Time of instance update
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new
            current time.
        '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
            convert created_at and updated_at atributes as
            string object in ISO format.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (cp_dct)
