#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
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
                if type(val) is cls:
                    final_list[key] = val
            return final_list

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes object from storage dictionary"""
        if obj is not None:
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

    def close(self):
        """
        This invokes the reload method
        """
        self.reload()

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                try:
                    temp = json.load(f)
                except FileNotFoundError:
                    pass

                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except BaseException:
            pass
