#!/usr/bin/python3
# 2-my_filter_states.py
# Author: @tonybnya
"""
This script takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


def main():
    """
    Main function
    """
    database = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    state_name = sys.argv[4]

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name \
                   LIKE BINARY %s ORDER BY states.id", (state_name))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
