#!/usr/bin/python3
""" This script takes state_name as argument and lists
    all cities of that state from database """
import MySQLdb
from sys import argv


def list_some(username, password, database, state_name):
    """Displays all cities of specified database

    Args:
        username: username
        password: user password
        database: database name
        state_name: name of state
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
            """SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = LIKE BINARY '%{}%'
            ORDER BY cities.id ASC""".format(state_name)
    )
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    list_some(argv[1], argv[2], argv[3], argv[4])