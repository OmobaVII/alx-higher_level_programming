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
             WHERE name like "{:s}"
             ORDER BY id""".format(argv[4])
    cur.execute(query)
    for state in cur.fetchall():
        if state[1] == argv[4]:
            print(state)
    cur.close()
    db.close()
