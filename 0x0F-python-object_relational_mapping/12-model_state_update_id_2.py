#!/usr/bin/python3
"""
A script that changes the name of a state in
the object State in the database
hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    """not to be executed when imported"""
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()  # saves the changes made

    session.close()
