#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco" """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


def create_state_city(username, password, db_name):
    """Create the State "California" with the City "San Francisco" """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name="California", cities=[City(name="San Francisco")])

    session.add(new_state)
    session.commit()

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    create_state_city(sys.argv[1], sys.argv[2], sys.argv[3])
