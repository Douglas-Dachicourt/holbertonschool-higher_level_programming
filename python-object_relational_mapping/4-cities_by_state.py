#!/usr/bin/python3
"""

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
        database=database
    )

    c = db.cursor()

    query = """ SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    ORDER BY cities.id
    """
    c.execute(query)

    results = c.fetchall()

    for row in results:
        print(row)

    c.close()
    db.close()
