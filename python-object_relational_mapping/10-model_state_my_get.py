#!/usr/bin/python3
"""
    Script that prints the State object with the name passed as
    argument from the database 'hbtn_0e_6_usa'
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    DATABASE_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    state_arg = sys.argv[4]

    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like("{}".format(state_arg))).all()

    if not states:
        print("Not found")
    else:
        for state in states:
            print("{}".format(state.id))

    session.close()
