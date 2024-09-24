#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models import store_typ
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if store_typ == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
#        places = relationship('Place', backref=backref('user', cascade='all'))
#        reviews = relationship(
#                'Review',
#                backref=backref('user', cascade='all')
#            )
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        super().__init__(*args, **kwargs)
