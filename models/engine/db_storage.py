#!/usr/bin/python3
"""this has the class for DBStorage"""
import models
from os import environ
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base

classes = ["User", "State", "City", "Amenity", "Place", "Review"]


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
            environ["HBNB_MYSQL_USER"],
            environ["HBNB_MYSQL_PWD"],
            environ["HBNB_MYSQL_HOST"],
            environ["HBNB_MYSQL_DB"]), pool_pre_ping=True)
        if environ["HBNB_ENV"] == "test":
            Base.metadata.drop_al(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Returns:
            returns the dictionary of the object
        """
        if cls:
            for obj in
