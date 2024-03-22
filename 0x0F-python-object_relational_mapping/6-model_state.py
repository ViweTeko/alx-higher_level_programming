#!/usr/bin/python3
"""This script contains class definition of state and an
    instance Base = declarative_base()"""
import sys
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
