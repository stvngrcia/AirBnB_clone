#!/usr/bin/python3
'''
    Define class DBStorage
'''

import os
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base

class DBStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __engine = None
    __session = None


    def __init__(self):
        '''
            create new instance of DBStorage
        '''
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                 user, pwd, host, db), pool_pre_ping=True)
        # Create all the tables in the database which are
        # defined by Base's subclasses
        Base.metadata.create_all(self.__engine)

        if os.environ.get('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop(engine)


    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        dict_db = {}
        if cls != None:
            entry = self.__session.query(models.temp_cls[cls]).all()
            for obj in entry:
                # under the hood, sqlalchemy converts entry to objects
                # allowing access to object attributes
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dict_db[key] = obj
        else:
            for k, v in models.temp_cls.items():
                if k != "BaseModel":
                    for obj in self.__session.query(v).all():
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        dict_db[key] = obj
        return dict_db

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Arguments:
                obj : An instance object.
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        self.__session.commit()

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        # create a configured "Session" class 
        Session = sessionmaker(bind=self.__engine)
        # create a session
        session = Session()
        self.__session = session


    def delete(self, obj=None):
        '''
            Delete object from __object if exists
        '''

