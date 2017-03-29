#!/usr/bin/python3
"""
State Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ""
        cities = ""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            my_list = storage.all("City").values()
            c_list = [city_list for city in my_list if self.id == city.state_id]
            return c_list

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
