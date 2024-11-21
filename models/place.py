#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import store_typ
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship, backref


if store_typ == 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False
            ),
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False
            )
        )


class Place(BaseModel, Base):
    """ A place to stay """

    if store_typ == 'db':
        __tablename__ = 'places'

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
        amenities = relationship(
                'Amenity', secondary=place_amenity, viewonly=False,
                backref='place_amenities')
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

    if store_typ != 'db':
        @property
        def reviews(self):
            """returns the list of City instances with state_id"""
            from models import storage
            from models.review import Review

            rev_list = []

            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    rev_list.append(review)

            return rev_list

        @property
        def amenities(self):
            """returns the list of City instances with state_id"""
            from models import storage
            from models.amenity import Amenity

            amn_list = []

            for amenity in storage.all(Amenity).values():
                if amenity.id in self.id:
                    amn_list.append(amenity)

            return amn_list

        @amenities.setter
        def amenities(self, obj):
            """Returns the list of Amenity instances"""
            self.amenity_ids.append(obj.id)
