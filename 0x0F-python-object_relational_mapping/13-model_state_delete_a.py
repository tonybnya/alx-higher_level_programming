#!/usr/bin/python3
# 13-model_state_delete_a.py
# Author: @tonybnya
"""
This script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Main function. """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).filter(State.name.like('%a%')) \
        .delete(synchronize_session='fetch')

    session.commit()
    session.close()


if __name__ == '__main__':
    main()
