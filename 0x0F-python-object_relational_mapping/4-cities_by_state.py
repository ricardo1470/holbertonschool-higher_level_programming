#!/usr/bin/python3
""" script that takes in arguments
    and displays all values in the states
    table of hbtn_0e_0_usa where name matches
    the argument. But this time, write one that
    is safe from MySQL injections!"""


from sys import argv
import MySQLdb

if __name__ == '__main__':

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]

    db = MySQLdb.connect(
        "localhost",
        my_user,
        my_pass,
        my_db
    )

    cur = db.cursor()
    database = cur.execute("SELECT cities.id, cities.name, states.name \
                         FROM cities JOIN states ON cities.state_id = \
                         states.id ORDER BY cities.id;")
    for i in range(0, database):
        results = cur.fetchone()
        print("{}".format(results))

    cur.close()
    db.close()
