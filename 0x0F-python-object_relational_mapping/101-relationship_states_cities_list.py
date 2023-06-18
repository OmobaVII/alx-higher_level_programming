#!/usr/bin/python3
"""
the module lists all State objects
corresponding City objects
from the database hbtn_0e_101_usa
"""
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """does not execute when imported"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    full_db = session.query(State).order_by(State.id)
    for state in full_db:
        print("{:d}: {:s}".format(state.id, state.name))
        for city in state.cities:
            print("    {:d}: {:s}".format(city.id, city.name))

    session.close()
