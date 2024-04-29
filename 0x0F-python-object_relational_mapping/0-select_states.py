#!/usr/bin/python3
""" list states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = argv[1],
        passwd = argv[2],
        db = argv[3],
        charset="utf8"

    )
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    records = cur.fetchall()
    for record in records:
        print(record)
    cur.close()
    con.close()
