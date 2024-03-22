#!/usr/bin/python3
""" This script displays all stats starting with N """
import sys
from sys import argv
import MySQLdb


def state_some(username, password, database, state_name):
    """ Lists states starting with N

    Args:
        username: user name
        password: password
        database: database name
        state_name: name of state
    """
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            db=database,
            port=3306
    )
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                    WHERE name LIKE BINARY '{}'
                    ORDER BY states.id ASC""".format(state_name)
                   )
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <script> <username> <password> <database> <state name>")
        exit(1)
    state_some(argv[1], argv[2], argv[3], argv[4])
