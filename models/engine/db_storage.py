#!/usr/bin/python3
'''
    Define class DBStorage
'''

from os import getenv
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
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
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                 user, pwd, host, db), pool_pre_ping=True)
        # Create all the tables in the database which are
        # defined by Base's subclasses
        Base.metadata.create_all(self.__engine)

        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        '''
            Return a dictionary of SQL objects
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
            Set in obj as a database entry
            Arguments:
                obj : An instance object.
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commit the saves to database
        '''
        self.__session.commit()

    def reload(self):
        '''
            Starts a global session
        '''
        # create a configured factory class 
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # create a global session for all to use
        Session = scoped_session(factory)
        self.__session = Session()


    def delete(self, obj=None):
        '''
            Delete object from database if exists
        '''
        if obj is not None:
            self.__session.delete(obj)
