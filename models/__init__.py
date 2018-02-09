#!/usr/bin/python3
'''
    Package initializer
'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
