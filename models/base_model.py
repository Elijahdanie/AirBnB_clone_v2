#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql.expression import delete
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """initializes the basemodel class"""
        if (not kwargs):
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at
            self.created_at = datetime.utcnow()
        elif kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, BaseModel.TIME_FORMAT)
                    setattr(self, key, value)
            if not hasattr(kwargs, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(kwargs, 'updated_at'):
                setattr(self, 'updated_at', datetime.utcnow())
            if not hasattr(kwargs, 'created_at'):
                setattr(self, 'created_at', datetime.utcnow())

    def __str__(self):
        """Returns a string representation of the instance"""
        format_dict = self.__dict__.copy()
        if '_sa_instance_state' in format_dict.keys():
            del format_dict['_sa_instance_state']
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, format_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict

    def delete(self):
        from models import storage
        storage.delete(self.id)
