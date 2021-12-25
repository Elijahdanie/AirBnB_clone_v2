#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import (
    BaseModel,
    Base
)
from sqlalchemy import (
    Column, 
    String
)
from sqlalchemy.orm import (
    relationship,
    backref
)
from os import getenv

class State(BaseModel, Base):
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE', '') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all("City")
            temp = []
            for c_id in all_cities:
                if all_cities[c_id].state_id == self.id:
                    temp.append(all_cities[c_id])

            return temp