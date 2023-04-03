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
        host="localhost",
        port="3306",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf-8"
    )
    state_name = sys.argv[4]

    cursor = database.cursor()
    query = ' '.join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "WHERE states.name LIKE BINARY '{}'",
        "ORDER BY cities.id",
    ]).format(state_name)

    cursor.execute(query)
    result = cursor.fetchall()
    str_result = ', '.join([i[0] for i in result])

    print(str_result)

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
