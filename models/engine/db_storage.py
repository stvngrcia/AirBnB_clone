#!/usr/bin/python3
"""Prints all City objects from database
"""

import MySQLdb
import sqlalchemy
import sys
from models.base_model import BaseModel, Base
from models.state import State
from model.city import City
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm import scoped_session
from os import getenv

__engine = None
__session = None

user = getenv('HBNB_MYSQL_USER')
pswd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
environ = getenv('HBNB_ENV')

def __init__(self):
    self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                pswd,
                                                host,
                                                db),
        pool_pre_ping=True)

    if (environ == 'test'):
        Base.metadata.drop_all(bind=engine)

'''        for state, city in session.query(State, City)\
            .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
'''
def all(self, cls=None):
    obj_dict = {}
    if cls is not None:
        for val in self.__session.query(cls):
            '''Should return class name.object id'''
            key = val.__class__.__name__ + "." + val.id
            obj_dict[key] = val
'''    else:
        for val in self.__session.query(
'''        


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

    Session = sessionmaker(bind=engine, expire_on_commit=False)

    S = scoped_session(Session)

    self.__session = S()
