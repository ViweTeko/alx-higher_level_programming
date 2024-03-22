#!/usr/bin/python3
""" This script lists all cities from database """
import MySQLdb
from sys import argv


def list_cities(username, password, database):
    """ Displays all cities in database

    Args:
        username: Username
        password: user password
        database: database name
    """
    db = MySQL.connect(
            host="localhost",
            user=username,
            password=password,
            db=database,
            port=3306
    )
    cursor = db.cursor()
    cursor.execute(
            """SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC"""
    )
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    list_cities(argv[1], argv[2], argv[3])
