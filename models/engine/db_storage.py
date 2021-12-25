#!/usr/bin/python3
"""
database storage engine
"""
import os
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

# try to import config if available
try:
    from decouple import config as get_env
except ImportError:
    get_env = os.environ.get

# environs and options
env = {
    # environment settings to use
    'environment': get_env('HBNB_ENV'),

    # db connections
    'mysql_user': get_env('HBNB_MYSQL_USER'),
    'mysql_passwd': get_env('HBNB_MYSQL_PWD'),
    'mysql_host': get_env('HBNB_MYSQL_HOST'),
    'mysql_db': get_env('HBNB_MYSQL_DB'),
    'mysql_port': 3306,
}


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

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
            env['mysql_user'],
            env['mysql_passwd'],
            env['mysql_host'],
            env['mysql_port'],
            env['mysql_db']),
            pool_pre_ping=True)

        try:
            if env['environment'] == 'test':
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

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
            if cls not in self.models.keys():
                return
            for instance in self.__session.query(cls).all():
                objects[instance.id] = instance

        else:
            # fetch all object instances instead
            for cls_name in self.models.keys():
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
        try:
            # try commiting
            self.__session.commit()
        except Exception:
            # if an exception occurs rollback the commit
            self.__session.rollback()
            raise
        finally:
            # end the database session
            self.__session.close()

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
