#!/usr/bin/python3
# 4-cities_by_state.py
# Author: @tonybnya
"""
This script lists all cities from the database hbtn_0e_4_usa.
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

    cursor = database.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY cities.id")

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
