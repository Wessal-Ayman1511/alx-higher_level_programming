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
    query = "SELECT c.id, c.name, s.name \
            FROM cities as c, states as s \
            WHERE c.state_id = s.id \
            ORDER BY c.id ASC"
    cur.execute(query)
    records = cur.fetchall()
    for record in records:
        print(record)
    cur.close()
    conn.close()
