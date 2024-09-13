#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import store_typ
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Amenity(BaseModel, Base):
    """Amenity Model"""

    if store_typ == 'db':
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        super().__init__(*args, **kwargs)
