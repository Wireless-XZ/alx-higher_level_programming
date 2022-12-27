#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM states INNER JOIN cities
    ON cities.state_id = states.id
    ORDER BY cities.id;
    """)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
