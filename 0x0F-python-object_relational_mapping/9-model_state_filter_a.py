#!/usr/bin/python3
""" This script lists all States containing the letter a"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def state_a(username, password, database):
    """Displays all states containing 'a'
    Args:
        username: username
        password: user password
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
            print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    state_a(argv[1], argv[2], argv[3])
