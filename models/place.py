#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Float, String, Column, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


place_amenity = Table('place_amenity', Base.metadata,
                Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
                Column('amenity_id', String(60), ForeignKey('amenities.id'),
                    nullable=False))
class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
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
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    @property
    def reviews(self):
        '''Getter method that returns the list of Review instances for
        FileStorage engine.'''
        review_list = []
        for review in self.reviews:
            if self.id == review.place_id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        '''Getter method that returns the list of Amenities instances for
        FileStorage engine.'''
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        '''
            Setter method that handles appending Amenity instances to a list. If
            `val` is not an Amenity object, it won't be appended to the list.
        '''
        for amenities in self.amenities:
            if self.id == amenities.place_id and \
                    obj.__class__.__name__ == 'Amenity':
                amenity_ids.append(obj)
