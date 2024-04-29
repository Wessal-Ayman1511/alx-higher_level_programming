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
    query = "SELECT c.name\
            FROM cities as c join states as s \
            on c.state_id = s.id\
            WHERE s.name LIKE %s \
            ORDER BY c.id ASC"
    cur.execute(query, (argv[4], ))
    records = cur.fetchall()
    print(", ".join(city[0] for city in records))
    cur.close()
    conn.close()
