#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states; ORDER BY states.id ASC;")

    for state_name in cursor:
        print(state_name)
