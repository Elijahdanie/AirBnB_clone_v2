#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

if os.environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = FileStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    
storage.reload()
