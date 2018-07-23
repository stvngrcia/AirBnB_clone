#!/usr/bin/python3
"""this has the class for DBStorage"""
import models
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = [User, State, City, Place, Review, Amenity]


class DBStorage:
    """this is the Databse storage
    Attributes:
        __engine: initialize with None
        __session: initialize with None
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instance attribute for DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Returns:
            returns the dictionary of the object
        """
        obj = {}
        if cls:
            for value in self.__session.query(cls):
                key = str(value.__class__.__name__) + "." + str(value.id)
                obj[key] = value
        else:
            for one_class in classes:
                for value in self.__session.query(one_class):
                    key = str(value.__class__.__name__) + "." + str(value.id)
                    obj[key] = value
        return obj

    def new(self, obj):
        """creating new object
        Args:
            obj: the new object being created
        """
        self.__session.add(obj)

    def save(self):
        """saving session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delets obj in session
        Args:
            obj: obj to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """relaodign session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
