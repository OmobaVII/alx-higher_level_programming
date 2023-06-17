#!/usr/bin/python3
"""
A python script that
Lists the first state objects from the database
hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """so if imported does not execute"""

    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("{:d}: {:s}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
