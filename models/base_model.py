#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from models import store_typ

if store_typ == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if store_typ == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(
                DateTime, nullable=False,
                default=datetime.utcnow()
            )
        updated_at = Column(
                DateTime, nullable=False,
                default=datetime.utcnow()
            )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if store_typ == 'fs':
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        self.id = str(uuid.uuid4())
        for k, v in kwargs.items():
            if k == '__class__':
                continue

            self.__dict__.update(kwargs)
            if k in ['updated_at', 'created_at'] and type(v) is str:
                kwargs[k] = datetime.strptime(
                        kwargs[k],
                        '%Y-%m-%dT%H:%M:%S.%f'
                    )

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}

        dictionary.update(self.__dict__)

        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
