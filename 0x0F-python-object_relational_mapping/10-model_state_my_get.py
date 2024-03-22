#!/usr/bin/python3
""" This script prints State object with name passed as arg"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def obj_state(username, password, database, state_name):
    """ Displays state object

    Args:
        username: username
        password: user password
        database: database name
        state_name: name of state
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    with session_maker() as session:
        states = session.query(State).filter_by(
                name=state_name).order_by(State.id).all()
        if states:
            for state in states:
                print(state.id)
            else:
                print("Not found")


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <script> <username> <password> <database> <state name>")
        sys.exit(1)
    obj_state(argv[1], argv[2], argv[3], argv[4])
