#!/usr/bin/python3
"""Inserts into State obj from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def insert_to_state_obj():
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)
        state = State(name='Louisiana')

        session.add(state)
        session.commit()
        print(state.id)

        session.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    insert_to_state_obj()
