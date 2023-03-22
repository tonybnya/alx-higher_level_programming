#!/usr/bin/python3
# 5-filter_cities.py
# Author: @tonybnya
"""
This script takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa.
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
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id WHERE states.name=%s \
        ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
