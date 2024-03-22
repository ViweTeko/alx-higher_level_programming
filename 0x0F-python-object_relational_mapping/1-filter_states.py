#!/usr/bin/python3
""" This script displays states starting with N"""
import MySQLdb
from sys import argv


def state_all(username, password, database):
    """ Lists all states starting with N"""
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            db=database
            port=3306
    )
    cursor = db.cursor()
    cursor.execute(
            """SELECT * FROM states WHERE name LIKE BINARY 'N%'
            ORDER BY states.id ASC
            """)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <script> <username> <password> <database>")
        exit(1)
    state_all(argv[1], argv[2], argv[3])
