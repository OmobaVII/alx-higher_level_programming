#!/usr/bin/python3
"""
the module prints all City objects
from the database hbtn_0e_14_usa
"""
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """does not execute when imported"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    sque = "State.name, City.id, City.name"

    for state, c_id, c_name in session.query(State.name, City.id, City.name).\
            filter(State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(state, c_id, c_name))

    session.close()
