#!/usr/bin/python3
# 10-model_state_my_get.py
# Author: @tonybnya
"""
This script prints the State pbject with the name passed as argument
from the database hbtn_0e_6_usa
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
    result = session.query(State).filter_by(name=sys.argv[4]).first()

    if result:
        print(f"{result.id}")
    else:
        print("Not found")

    session.close()


if __name__ == '__main__':
    main()
