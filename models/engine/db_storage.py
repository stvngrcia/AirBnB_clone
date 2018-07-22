#!/usr/bin/python3
'''
    Define class FileStorage
'''

import os
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __engine = None
    __session = None


    def __init__(self):
        '''
            create new instance of DBStorage
        '''
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')

        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                 user, pwd, host, db), pool_pre_ping=True)

        # Create all the tables in the database which are
        # defined by Base's subclasses
        Base.metadata.create_all(engine)
        # create a configured "Session" class 
        Session = sessionmaker(bind=engine)
        # create a session
        session = Session()
        
        if os.environ.get('HBNB_MYSQL_ENV') == 'env':
            Base.metadata.drop(engine)

    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        return self.__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Arguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
            Delete object from __object if exists
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        remove = [k for k in FileStorage.__objects.keys() if k == key]
        for k in remove:
            del FileStorage.__objects[k]
        FileStorage().save()
