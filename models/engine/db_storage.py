#!/usr/bin/python3
"""
Creating a new engine that
manages database storage
"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes
        """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                 getenv('HBNB_MYSQL_USER'),
                 getenv('HBNB_MYSQL_PWD'),
                 getenv('HBNB_MYSQL_HOST'),
                 getenv('HBNB_MYSQL_DB')))
        self.__my_list = {"User": User, "State": State, "City": City,
                          "Amenity": Amenity, "Place": Place, "Reivew": Review}
        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        all
        """
        new_dict = {}
        if cls is None:
            for x in self.__my_list.values():
                if self.__session.query(x).all():
                    for item in self.__session.query(x).all():
                        new_dict[item.id] = item
        else:
            for item in self.__session.query(self.__my_list[cls]):
                new_dict[item.id] = item
        return (new_dict)

    def new(self, obj):
        """
        new
        """
        self.__session.add(obj)

    def save(self):
        """
        save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
       delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
       reload
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        self.__session.remove()
