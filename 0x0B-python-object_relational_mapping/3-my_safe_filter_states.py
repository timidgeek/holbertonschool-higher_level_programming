#!/usr/bin/python3
""" Script that  takes in an argument and
    displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument,
    AND script must be safe from MySQL injections"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                   ORDER BY states.id ASC;")

    for state_name in cursor:
        if state_name[1] == sys.argv[4]:
            print(state_name)
