#!/usr/bin/python3

"""
    Script that prints the first State object from the database 'hbtn_0e_6_usa'
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    DATABASE_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    states = session.query(State).all()

    if states == "":
        print()
    else:
        for state in states:
            if state.id == 1:
                print("{}: {}".format(state.id, state.name))

    session.close()
