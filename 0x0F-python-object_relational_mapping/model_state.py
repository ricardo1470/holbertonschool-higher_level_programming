#!/usr/bin/python3
"""State class:
    inherits from Base
    links to the MySQL table states """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ create table """
    __tablename__ = "states"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
