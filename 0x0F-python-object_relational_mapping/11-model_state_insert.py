#!/usr/bin/python3
"""This script adds Louisiana state to database"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def add_state(username, password, database):
    """Adds Louisiana state to database
    Args:
        username: username
        password: password
        database: database
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    with session_maker() as session:
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    add_state(argv[1], argv[2], argv[3])
