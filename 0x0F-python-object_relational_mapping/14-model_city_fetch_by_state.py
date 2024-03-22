#!/usr/bin/python3
"""This script prints all city objects from database"""
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def all_cities(username, password, database):
    """Prints all city objects from database

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
        cities = session.query(City).join(State).order_by(City.id).all()
        for city in cities:
            print("{}: ({}) {}".format(city.state.name, city.id, city.name))


if __name == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    all_cities(argv[1], argv[2], argv[3])
