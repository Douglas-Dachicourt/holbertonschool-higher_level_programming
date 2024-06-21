#!/usr/bin/python3
"""
    Script 14-model_city_fetch_by_state.py that prints all City objects from
    the database 'hbtn_0e_14_usa'
"""

if __name__ == "__main__":
    from model_city import City
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    DATABASE_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(
        State, City.state_id == State.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
