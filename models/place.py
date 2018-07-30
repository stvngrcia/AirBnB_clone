#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity ", secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """This is the property setter for reviews
        Return:
            all object in list
        """
        get_all = models.storage.all("Review").values()
        return [obj for obj in get_all if obj.place_id == self.id]

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """This is the property setter for reviews
            Return:
                all object in list
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """setting for amenities"""
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
