#!/usr/bin/python3
# 12-model_state_update_id_2.py
# Author: @tonybnya
"""
This script changes the name of a State object from
the database hbtn_0e_6_usa
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
    result = session.query(State).filter(State.id == 2) \
        .update({"name": "New Mexico"}, synchronize_session='fetch')

    session.commit()
    session.close()


if __name__ == '__main__':
    main()
