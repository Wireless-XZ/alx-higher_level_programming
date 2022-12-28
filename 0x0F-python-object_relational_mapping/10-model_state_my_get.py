#!/usr/bin/python3
"""
a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)()

    x = 0
    for state in session.query(State).order_by(State.id):
        if state.name == argv[4]:
            x = 1
            print(state.id)

    if x == 0:
        print("Not found")
