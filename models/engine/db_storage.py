#!/usr/bin/python3
"""Prints all City objects from database
"""

import MySQLdb
import sqlalchemy
import sys
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm import scoped_session
from os import getenv
import models


user = getenv('HBNB_MYSQL_USER')
pswd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
environ = getenv('HBNB_ENV')



class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                 pswd,
                                                 host,
                                                 db),
            pool_pre_ping=True)

        if (environ == 'test'):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        # cls = str
        if cls is not None:
            for val in self.__session.query(models.tmp_classes[cls]):
                '''Should return class name.object id'''
                key = str(val.__class__.__name__) + "." + str(val.id)
                obj_dict[key] = val
                return obj_dict
        else:
            for val in self.__session.query(State, City):
                key = val.__class__.__name__ + "." + val.id
                obj_dict[key] = val
                return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
    '''do we need to commit or call save?'''

    def reload(self):
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        S = scoped_session(Session)

        self.__session = S()
