#!/usr/bin/python3
"""
A script that lists all states from the
database hbtn_0e_0_usa
The script takes 3 arguments
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
    cur.execute("SELECT * FROM states ORDER BY id")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
