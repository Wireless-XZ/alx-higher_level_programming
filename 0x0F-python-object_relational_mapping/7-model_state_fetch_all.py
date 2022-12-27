#!/usr/bin/python3
"""
 lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

session = sessionmaker(bind=engine)()

for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
