#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   join states ON cities.state_id = states.id \
                   ORDER BY cities.id ASC;")
    gettem = cursor.fetchall()

    for row in gettem:
        print(row)
