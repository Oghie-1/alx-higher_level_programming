#!/usr/bin/python3
"""List first State object from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_first_state_obj():
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        first_state = session.query(State).first()

        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        session.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    list_first_state_obj()
