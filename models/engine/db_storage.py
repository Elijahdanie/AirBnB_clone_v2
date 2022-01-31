#!/usr/bin/python3
"""
database storage engine
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy import create_engine
from models import (
    amenity,
    city,
    state,
    place,
    review,
    user,
)
from models.base_model import Base

from os import getenv


# class definition starts here
class DBStorage:
    """A database storage engine class
    """
    __engine = None
    __session = None

    # mapped each models to a dict key
    models = {
        'Amenity': amenity.Amenity,
        'City': city.City,
        'User': user.User,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State
    }

    def __init__(self):
        """instantiates engine
        """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
            .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """retrieves all object instance

        Args:
            cls ([class.BaseModel], optional): [BaseModel model].
            Defaults to None.

        Returns:
            [dict]: Returns a dictionary of instances
        """
        objects = {}

        if cls is not None:
            # fetch a specific object instance
            if cls not in self.models.values():
                return
            for instance in self.__session.query(cls).all():
                objects[instance.id] = instance

        else:
            # fetch all object instances instead
            for cls_name in self.models.values():
                for instance in self.__session.query(cls_name).all():
                    objects[instance.id] = instance

        return objects

    def new(self, obj):
        """adds a new object to the current database session

        Args:
            obj (class.BaseModel): [description]
        """
        self.__session.add(obj)

    def save(self):
        """commits the new objects to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes a table from the database

        Args:
            obj (database table name, optional): [description].
            Defaults to None.
        """
        if obj is None:
            return

        try:
            self.__session.delete(obj)
        except Exception:
            raise

    def reload(self):
        """reloads all a objects from the database
        """
        Amenity = self.models['Amenity']
        City = self.models['City']
        User = self.models['User']
        Place = self.models['Place']
        State = self.models['State']

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))

    def close(self):
        """
        Closes the SQLAlchemy session
        """
        self.__session.close()
