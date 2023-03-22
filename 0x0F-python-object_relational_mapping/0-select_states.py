#!/usr/bin/python3
# 0-select_states.py
# Author: @tonybnya
"""
This script lists all states from the database hbtn_0e_0_usa
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

    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")

    for state in cur.fetchall():
        print(state)

    cur.close()
    database.close()


if __name__ == "__main__":
    main()
