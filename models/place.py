#!/usr/bin/python3
'''
    Define the class Place.
'''

from os import getenv
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Table, MetaData, Float
import models

storage_type = getenv('HBNB_TYPE_STORAGE')
metadata = MetaData()

place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey("places.id"),
                             nullable=False,
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey("amenities.id"),
                             nullable=False,
                             primary_key=True),
                  )


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    if (storage_type == 'db'):
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete-orphan", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        @property
        def get_reviews(self):
            review_list = []
            for val in storage.all(Review).values():
                if val.place_id == place.id:
                    review_list.append(val)
            return review_list
        @property
        def get_amenities(self):
            amenity_list = []
            for val in storage.all(Amenity).values():
                if val.amenity_id == amenity.id:
                    amenity_list.append(val)
            return amenity_list
