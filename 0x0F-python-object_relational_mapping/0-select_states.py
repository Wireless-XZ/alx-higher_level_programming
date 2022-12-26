#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

    cur.close()
conn.close()
