#!/usr/bin/python3
"""
A python script that
Lists all state objects from the database
hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                       format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(State).order_by(State.id):
    print("{:d}: {:s}".format(instance.id, instance.name))
session.close()
