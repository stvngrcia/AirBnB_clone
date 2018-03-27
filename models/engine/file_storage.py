#!/usr/bin/python3
'''
    FileStorage Engine
'''
import json
import models
import os


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Returns all objects. The format depends on the value of the
            environment variable 'HBNB_TYPE_STORAGE'. If it is 'file', this
            method will return a dictionary of objects that have been formatted
            using the `new()` method. If it is 'db', a list of all objects in
            the MySQL database will be returned.
        '''
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            pass
            # do db
        elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
            return self.__objects
        else:
            print('Invalid file storage type. Check the HBNB_TYPE_STORAGE' +
                  'environment variable. It needs to be \'db\' or \'file\'')
            return

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

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
           Deletes an object from FileStorage__objects if it exists.
        '''
        if obj is None:
            return
        # Using dictionary comprehension to delete an item from
        # FileStorage.__objects if the value is the object (`obj`) being passed
        # to this method
        FileStorage.__objects = {k: v for k, v in FileStorage.__objects.items()
                                 if v.id != obj.id}
