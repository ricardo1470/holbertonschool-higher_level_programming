#!/usr/bin/python3
""" script that takes in the name
    of a state as an argument and
    lists all cities of that state,
    using the database hbtn_0e_4_usa """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    my_user = argv[1]
    my_pass = argv[2]
    my_db = argv[3]
    name_s = argv[4]
    list_cities = []

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
        if results[2] == name_s:
            list_cities.append(results[1])

    for i in range(0, len(list_cities)):
        print("{}".format(list_cities[i]), end=", "
              if i < len(list_cities) - 1 else "\n")

    if len(list_cities) == 0:
        print()

    cur.close()
    db.close()
