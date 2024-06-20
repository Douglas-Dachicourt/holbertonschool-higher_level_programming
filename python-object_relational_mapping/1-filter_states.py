#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database 'hbtn_0e_0_usa'
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database)

    c = db.cursor()
    c.execute("""SELECT * FROM states
    ORDER BY id""")
    results = c.fetchall()

    for row in results:
        if row[1][0] == "N":
            print(row)
