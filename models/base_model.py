#!/usr/bin/python3
'''
'''
import uuid
import datetime
class BaseModel:
    '''
    '''
    def __init__(self):
        '''
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        '''
        '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''
        '''
        copy_dict = dict(self.__dict__)
        copy_dict['__class__'] = self.__class__.__name__
        copy_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        copy_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (copy_dict)
