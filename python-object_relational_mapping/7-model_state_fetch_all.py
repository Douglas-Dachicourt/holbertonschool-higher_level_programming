#!/usr/bin/python3
"""
    Script that lists all State objects from the database hbtn_0e_6_usa

"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    import sys

    # Address of the data base URL
    DATABASE_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    # Connection through the database with engine module
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Creation of a session
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    # Find all results
    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
