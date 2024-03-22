#!/usr/bin/python3
"""This script lists all State objects from database"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def list_states(username, password, database):
    """ Displays all states in database

    Args:
        username: username
        password: user password
        database: the database
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    with session_maker() as session:
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    list_states(argv[1], argv[2], argv[3])
