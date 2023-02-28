#!/usr/bin/python3
"""Script that lists all State objects
    from the database hbtn_0e_6_usa which
    contain letter 'a'"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import MySQLdb
import sys

if __name__ == "__main__":
    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the database for all states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')) \
                    .order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
