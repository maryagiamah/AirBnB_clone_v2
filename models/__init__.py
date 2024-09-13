#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

store_typ = os.environ.get('HBNB_TYPE_STORAGE')


if store_typ == 'db':
    from models.engine.db_storage import DBStorage
    from models.user import User
    from models.place import Place
    from models.amenity import Amenity
    from models.review import Review
    from models.state import State
    from models.city import City
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
