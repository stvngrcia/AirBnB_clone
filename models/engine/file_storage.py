#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json

class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file
        to instances.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            return the dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
            set in __objects the obj with key <obj class name>.id
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj.to_dict()
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            serializes __objects attribute to JSON file.
        '''
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
           json.dump(FileStorage.__objects,fd)

    def reload(self):
        '''
            deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, mode='r', encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
        except FileNotFoundError:
            pass
