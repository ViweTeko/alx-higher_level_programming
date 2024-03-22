#!/usr/bin/python3
""" This script displays states starting with N"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Lists all names starting with N"""
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            db=argv[3],
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
