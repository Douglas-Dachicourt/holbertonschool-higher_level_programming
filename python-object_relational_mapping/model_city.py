#!/usr/bin/python3
"""
    Module that contains the class definition of a State
and an instance Base = declarative_base():

Classes:
    City

Attributes:
    Base: declarative_base from SQLAlchemy

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Class City that inherits from Base

        Table: city we want to establish in the DB

        Attributes:

        - id: integer, can not be NULL, is unique and
        is PRIMARY KEY

        - name: string, can not be NULL and is limited
        to 128 char

        -state_id = a foreign key in relation with State model

    """
    __tablename__ = "cities"

    id = Column(Integer, unique=True, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
