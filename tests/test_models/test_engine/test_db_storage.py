#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "only testing db storage")

class test_DBStorage(unittest.TestCase):

    def setup(self):
        env = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db, pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.session = Session()

    def testState(self):
        state = State(name="Greg")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Greg")

    def testCity(self):
        city = City(name="Afa")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Afa")

    def testPlace(self):
        place = Place(name="MyShoeBox", number_rooms=5)
        if place.id in models.storage.all():
            self.assertTrue(place.number_rooms, 5)
            self.assertTrue(place.name, "MyShoeBox")

    def testUser(self):
        user = User(name="Young_Jeezy")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Young_Jeezy")

    def teardown(self):
        self.session.close()
        self.__transaction.rollback()
