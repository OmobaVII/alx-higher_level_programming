#!/usr/bin/python3
"""
A script that lists all states from the
database hbtn_0e_0_usa
The script takes 4 arguments
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """all code insdie this block wont be
    excuted if imported"""

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    query = """SELECT *
             FROM states
             WHERE name like %s
             ORDER BY id"""
    cur.execute(query, (argv[4],))  # Trailing comma added to create a tuple
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
