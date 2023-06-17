#!/usr/bin/python3
"""
A script that adds data to
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

    new_state = State(name="Louisiana")
    session.add(new_state)  # adds the state to the table
    session.commit()  # saves the changes made

    print(new_state.id)
    session.close()
