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
    query = """SELECT `cities` as `c` INNER JOIN `states` as `s` \
    ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id`
    """
    cursor.execute(query)

    print(', '.join([c[2] for c in cursor.fetchall() if c[4] == state_name]))

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
