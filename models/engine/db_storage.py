#!/usr/bin/python3
'''
    DBStorage Engine
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
import models
from models.city import City
from models.state import State
user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
database = os.getenv('HBNB_MYSQL_DB')


class DBStorage:
    '''
        DBStorage Class
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            DBStorage constructor
        '''
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        # Request a connection with the database once required
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        # Base gets some metadata when it is created (in models/base_model).
        # The metadata contains all the info we need to create the tables.
        Base.metadata.create_all(self.__engine)

        # If we are testing, we will drop all the tables. Why ??
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Start talking to the db
        Session = sessionmaker(bind=self.__engine)

        # Session is a SQLAlchemy class. self.__session is an instance.
        self.__session = Session()

    def all(self, cls=None):
        '''
            Queries all objects of a class in the database. If cls is None it
            will display all objects in the database
        '''
        all_objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj
        else:
            db_list = [City, State]
            for cls in db_list:
                for obj in self.__session.query(cls).all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    all_objects[key] = obj
        return all_objects

    def new(self, obj):
        '''
            Adds an object to the current database session.
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commits an object to the current database session.
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Deletes an object fromn the current database session
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
            Reloads all tables in the database
        '''
        # Request a connection with the database once required
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
