#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
import os
from datetime import datetime
import models
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# SQLAlchemy's declarative system that lets us to map
# classes and objects to tables in our database.
#if os.getenv('HBNB_STORAGE_TYPE') == 'db':
Base = declarative_base()


class BaseModel:
    '''
        Base class for all models. Each model will be given `id`, `created_at`
        and `updated_at` during initialization. Other instance attributes may
        be added via kwargs.
    '''

    # Class attributes for our database. These will represent Columns in the
    # table designated for that specific model (ex: State => `states`)
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes `id`, `created_at` and
            `updated_at` (and others via kwargs)
        '''
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            '''
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
                kwargs['created_at'] = datetime.now()
                kwargs['updated_at'] = datetime.now()
                for key, val in kwargs.items():
                    if "__class__" not in key:
                        setattr(self, key, val)
            '''
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
        if kwargs:
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)


    def __str__(self):
        '''
            Return string representation of a model.
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of a model.
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Updates the updated_at attribute, then, depending on the
            HBNB_STORAGE_TYPE environment variable, it will either add the
            object to FileStorage.__objects and save to JSON, or create an
            entry in the database.
        '''
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            Return a dictionary representation of a model. If the key
            `_sa_instance_state` exists in the model's __dict__, it will be
            removed.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        # remove the key '_sa_instance_state' if it exists
        cp_dct = {k: v for k, v in cp_dct.items() if k != '_sa_instance_state'}

        return cp_dct

    def delete(self):
        '''
           Deletes the object by calling the object's storage.delete() method.
        '''
        models.storage.delete(self)
