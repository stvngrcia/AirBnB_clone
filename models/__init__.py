#!/usr/bin/python3
'''
    Package initializer
'''
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    classes = {"User": User, "BaseModel": BaseModel,
               "Place": Place, "State": State,
               "City": City, "Amenity": Amenity,
               "Review": Review}

    storage = FileStorage()
    storage.reload()
