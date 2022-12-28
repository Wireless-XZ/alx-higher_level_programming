#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)()

    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)
