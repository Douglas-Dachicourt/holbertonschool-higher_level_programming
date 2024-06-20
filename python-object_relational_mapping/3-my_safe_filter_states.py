#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of 'hbtn_0e_0_usa' where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database)

    c = db.cursor()
    query = """SELECT * FROM states
    WHERE name = %s
    ORDER BY id"""
    c.execute(query, (state,))

    results = c.fetchall()

    for row in results:
        if state in row:
            print(row)

    c.close()
    db.close()
