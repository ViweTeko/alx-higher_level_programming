#!/usr/bin/python3
""" This script print first State from database"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlqlchemy.orm import sessionmaker
from model_state import State


def first_state(username, password, database):
    """Displays first State from database
    Args:
        username: user name
        password: user password
        database: database name
    """
    engine =create_engine(
            "mysql+mysqldb://{}:{}@localhost/()".format(
                username, password, database),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)

    with session_maker() as session:
        state = session.query(State).order_by(State.id).first()
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    first_state(argv[1], argv[2], argv[3])
