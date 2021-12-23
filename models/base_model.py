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
    id = Column(String, nullable=False, autoincrement=True, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""


        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            del kwargs['__class__']
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        if ("_sa_instance_state" in dupe):
            dupe.pop("_sa_instance_state", 0)
        return dupe

    def delete(self):
        from models import storage
        storage.delete(self.id)