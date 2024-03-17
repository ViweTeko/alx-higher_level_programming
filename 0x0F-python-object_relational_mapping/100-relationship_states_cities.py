#!/usr/bin/python3
"""This script  creates the State “California” with the
City “San Francisco” from the database
"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State


def create_state(username, password, database):
    """Creates the State “California” with the
    City “San Francisco” from the database hbtn_0e_100_usa

    Args:
        username: username
        password: password
        database: database
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)

    with session_maker() as session:
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        session.add(city)
        session.commit()

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    create_state(argv[1], argv[2], argv[3])
