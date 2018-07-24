#!/usr/bin/python3
'''
    Package initializer
'''

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

temp_cls = {"State": State, "City": City}

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

if os.environ.get("HBNB_TYPE_STORAGE") == "db": 
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
