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

from models.city import City


class State(BaseModel, Base):
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE', '') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                        cascade="all, delete, delete-orphan")
    else:
        name = ''

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all(City)
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list