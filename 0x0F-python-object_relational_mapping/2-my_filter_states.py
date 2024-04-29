#!/usr/bin/python3
""" list states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC"
    cur.execute(query.format(argv[4]))
    records = cur.fetchall()
    for record in records:
        print(record)
    cur.close()
    conn.close()
