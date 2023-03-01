#!/usr/bin/python3
"""Script that lists the first State object
    from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
