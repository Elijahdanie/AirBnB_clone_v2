#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from json.decoder import JSONDecodeError


class FileStorage:
    """manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
         """Returns a dictionary of models currently in storage"""
         if cls is None:
             return FileStorage.__objects
         else:
             final_list = {}
             for key, val in FileStorage.__objects.items():
                 if val.__class__.__name__ == cls.__name__:
                     final_list[key] = val
             return final_list
    
    # def all(self, cls=None):
    #     if cls is None:
    #         return FileStorage.__objects

    #     storage = {}
    #     for obj_id in FileStorage.__objects:
    #         obj_cls = FileStorage.__objects[obj_id].__class__.__name__
    #         if cls == obj_cls:
    #             storage[obj_id] = FileStorage.__objects[obj_id]

    #     return storage

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes object from storage dictionary"""
        if obj != None:
            uid = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects.pop(uid)
        else:
            pass


    def save(self):
        """Saves storage dictionary to file"""
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    temp = json.load(f)
                except JSONDecodeError:
                    pass

                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
