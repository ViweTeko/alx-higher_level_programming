#!/usr/bin/python3
"""This script lists all City objects from the database"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def all_cities(username, password, database):
    """Lists all City objects from the database

    Args:
        username: Username
        password: User password
        database: Database name
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    with session_maker() as session:
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    all_cities(argv[1], argv[2], argv[3])
