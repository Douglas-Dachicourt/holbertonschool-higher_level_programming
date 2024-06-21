#!/usr/bin/python3
"""
    Script that deletes all State objects with a name containing the
    letter a from the database 'hbtn_0e_6_usa'
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

    states = session.query(State).all()

    letter = 'a'

    for state in states:
        if letter in state.name:
            session.delete(state)
            session.commit()
            print("{}: {}".format(state.id, state.name))

    session.close()
