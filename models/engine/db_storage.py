#!/usr/bin/python3
'''
    Define class DBStorage
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
import models
user = os.environ['HBNB_MYSQL_USER']
password = os.environ['HBNB_MYSQL_PWD']
host = os.environ['HBNB_MYSQL_HOST']
database = os.environ['HBNB_MYSQL_DB']
env = os.environ['HBNB_ENV']


class DBStorage:
    '''DBStorage Class'''
    __engine = None
    __session = None

    def __init__(self):
        '''DBStorage constructor'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if env == 'test':
            DBStorage.__table__.drop(self.__engine)

    def all(self, cls=None):
        '''Displays all objects of a class in the database'''
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        all_objects = {}
        if cls is None:
            for cls in models.classes.keys():
                for instance in self.__session.query(cls).all():
                    key = '{}.{}'.format(instance.name, instance.id)
                    all_objects[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = '{}.{}'.format(instance.name, instance.id)
                all_objects[key] = instance
        return all_objects

    def new(self, obj):
        '''Adds an object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commits an object to the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes an object fromn the current database session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Reloads all tables in the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        Session.configure(bind=self.__engine)
        self.__session = Session()
