#!/usr/bin/python3
"""
A script that lists all cities
from the database hbtn_0e_4_usa
Sorted in ascending by cities id
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """all code inside this block wont be
    executed if imported"""

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM states
               JOIN cities
               WHERE states.id = cities.state_id
               ORDER BY cities.id"""

    cur.execute(query)
    for city in cur.fetchall():
        print(city)

    cur.close()
    db.close()
