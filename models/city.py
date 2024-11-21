#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import store_typ


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if store_typ == 'db':
        __tablename__ = "cities"

        state_id = Column(
                String(60),
                ForeignKey('states.id'),
                nullable=False
            )
        name = Column(String(128), nullable=False)
        places = relationship(
                'Place',
                backref=backref('cities', cascade='all')
            )
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        super().__init__(*args, **kwargs)
