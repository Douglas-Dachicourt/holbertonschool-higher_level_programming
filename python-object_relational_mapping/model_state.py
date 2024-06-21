#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

"""
Python file that contains the class definition of a State
and an instance Base = declarative_base()


"""

Base = declarative_base()


class State(Base):
    """
        Class State that inherits from Base model

    """
    __tablename__ = "states"

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


db = MySQLdb.connect(
    host='localhost',
    port=3306
)
