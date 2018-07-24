#!/usr/bin/python3
'''
    Package initializer
'''

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

storage_type = getenv('HBNB_TYPE_STORAGE')

if (storage_type == 'db'):
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
