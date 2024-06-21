#!/usr/bin/python3

"""
Module that contains the class definition of a State
and an instance Base = declarative_base():

Classes:
    State

Attributes:
    Base: declarative_base from SQLAlchemy
    db: connexion to the database

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

# Using the Base for our classes (model for our DB)
Base = declarative_base()


class State(Base):
    """
        Class State that inherits from Base

        Table: state we want to establish in the DB

        Attributes:

        - id: integer, can not be NULL, is unique and
        is PRIMARY KEY

        - name: string, can not be NULL and is limited
        to 128 char

    """
    __tablename__ = "states"

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


db = MySQLdb.connect(
    host='localhost',
    port=3306
)
