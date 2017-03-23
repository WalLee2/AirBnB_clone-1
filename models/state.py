#!/usr/bin/python3
"""
State Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
