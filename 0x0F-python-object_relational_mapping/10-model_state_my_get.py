#!/usr/bin/python3
"""
A python script that
prints the state object id
with the name passed a parameter
from the database
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

    states = session.query(State).filter(State.name == argv[4]).first()
    if states is not None:
        print("{:d}".format(states.id))
    else:
        print("Not found")
    session.close()
