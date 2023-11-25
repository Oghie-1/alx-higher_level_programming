#!/usr/bin/python3
"""List all State objects from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_state_obj():
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        rows = session.query(State).all()

        for state in rows:
            print("{}: {}".format(state.id, state.name))

        session.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    list_state_obj()
