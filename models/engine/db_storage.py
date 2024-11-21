#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City


class DBStorage:
    """Database Storage"""

    __engine = None
    __session = None
    classes = {
            'Base': Base,
            'State': State,
            'City': City,
            'User': User,
            'Place': Place,
            'Review': Review,
            'Amenity': Amenity,
        }

    def __init__(self):
        """Create Engine"""

        self.user = os.environ.get('HBNB_MYSQL_USER')
        self.passwd = os.environ.get('HBNB_MYSQL_PWD')
        self.host = os.environ.get('HBNB_MYSQL_HOST')
        self.db = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(self.user, self.passwd, self.host, self.db),
                pool_pre_ping=True
            )

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name
        """

        all_d = {}

        if cls is None:
            for cls_name, cls_obj in self.classes.items():
                for obj in self.__session.query(cls_obj).all():
                    all_d[f"{cls_name}.{obj.id}"] = obj
        else:
            if cls in self.classes.values():
                for obj in self.__session.query(cls).all():
                    all_d[f"{cls.__name__}.{obj.id}"] = obj
        return all_d

    def new(self, obj):
        """add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and current database session"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        self.__session = scoped_session(session_factory)

    def close(self):
        """Remove session"""
        self.__session.remove()
