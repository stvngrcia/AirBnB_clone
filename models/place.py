#!/usr/bin/python3
'''
    Define the class Place.
'''
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import Table
from models.base_model import BaseModel



place_amenity = Table('place_amenity', Base.metadata,
                       Column('place_id', String(60),
                              ForeignKey('places.id'), nullable=False),
                       Column('amenity_id', String(60),
                              ForeignKey('places.id'), nullable=False)
 )


class Place(BaseModel):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete-orphan',
                           backref='place')
    amenities = relationship('Amenity', secondary="place-amenity",
                             backref="place_amenities", viewonly=False)
    @property
    def reviews(self):
        """
        Returns a list of Review instances with specific place id
        """
        review_inst = models.storage.all('Review').values()
        all_revs = [inst for inst in review_inst if inst.place_id == self.id]
        return all_revs


    @property
    def amenities(self):
        """
        Returns a list of amenity instances
        """
        for amenity in self.amenity_ids:
            amenity_inst = models.storage.all('Review').values()
            all_amenities = [inst for inst in amenity_inst]
        return all_amenities
