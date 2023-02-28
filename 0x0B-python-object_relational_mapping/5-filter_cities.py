#!/usr/bin/python3
"""Script that takes in the name of a state as an
    argument and lists all cities of that state,
    using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities \
                   INNER JOIN states \
                   ON cities.state_id = states.id \
                   ORDER BY cities.id ASC")

    print(", ".join(city_name[2] for city_name in cursor
                    if city_name[4] == sys.argv[4]))
