#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
        Base class for other classes to be used for the duration
        of this project.
    '''
    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
            Attributes:
                id: id of an instance
                created_at: Time of instance creation
                updated_at: Time of instance update
        '''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

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
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
            convert created_at and updated_at atributes as
            string object in ISO format.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cp_dct)
