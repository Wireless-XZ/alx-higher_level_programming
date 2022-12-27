#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""
    SELECT cities.name FROM cities
    WHERE cities.state_id = (SELECT id FROM states WHERE name=%s);
    ORDER BY cities.id ASC
    """, (sys.argv[4],))

    query_rows = cur.fetchall()

    if len(query_rows) == 0:
        print()
    else:
        for row in query_rows:
            if query_rows.index(row) != len(query_rows) - 1:
                print(row[0], end=", ")
            else:
                print(row[0])
