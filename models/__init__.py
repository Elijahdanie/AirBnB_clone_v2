#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
try:
    from decouple import config as get_env
except ImportError:
    get_env = os.environ.get

if get_env('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    
storage.reload()
