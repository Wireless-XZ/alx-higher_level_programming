#!/usr/bin/python3
"""
 prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)()

    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
