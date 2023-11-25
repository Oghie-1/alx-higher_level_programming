#!/usr/bin/python3
"""List the id of the State object containing the specified argument from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_arg_state_obj():
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        state = session.query(State).filter(State.name == sys.argv[4]).first()

        if state:
            print(state.id)
        else:
            print("Not Found")

        session.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    list_arg_state_obj()
