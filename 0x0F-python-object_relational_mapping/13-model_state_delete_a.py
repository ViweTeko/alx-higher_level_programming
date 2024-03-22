#!/usr/bin/python3
"""This script deletes all States containing letter 'a'"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def del_state(username, password, database):
    """Deletes all State objects containing letter 'a'
    
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
        states = session.query(State).filter(
                State.name.like("%a%")).order_by(State.id).all()
        for state in states:
            session.delete(state)
        session.commit()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    delete_state(argv[1], argv[2], argv[3])
