#!/usr/bin/python3
""" This script changes name of State object from database"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import State


def update_state(username, password, database):
    """ Changes State object
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
        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = "New Mexico"
            session.commit()

    if __name__ == "__main__":
        if len(argv) != 4:
            print("Usage: <script> <username> <password> <database> <state name>")
            exit(1)
        update_state(argv[1], argv[2], argv[3])
