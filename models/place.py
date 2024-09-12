#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import store_typ
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.review import Review
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if store_typ == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
                'Review',
                backref=backref('place', cascade='all')
            )
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

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """returns the list of City instances with state_id"""
        from models import storage

        rev_list = []

        for review in storage.all(Review).values():
            if review.place_id == self.id:
                rev_list.append(review)

        return rev_list
