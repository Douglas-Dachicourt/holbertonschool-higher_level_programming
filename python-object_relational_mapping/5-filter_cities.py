#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database
    )

    c = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name = '{}'
    ORDER BY cities.id
    """.format(state)

    c.execute(query)

    results = c.fetchall()

    t = ", ".join(row[0] for row in results)
    print(t)

    c.close()
    db.close()
