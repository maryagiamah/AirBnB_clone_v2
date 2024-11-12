#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models import store_typ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if store_typ == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City',
                backref=backref('state')
            )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        super().__init__(*args, **kwargs)

    if store_typ != 'db':
        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            from models.city import City
            from models import storage

            c_list = []

            for city in storage.all(City).values():
                if city.state_id == self.id:
                    c_list.append(city)

            return c_list
