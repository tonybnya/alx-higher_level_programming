#!/usr/bin/python3
# 0-select_states.py
# Author: @tonybnya
"""
This script lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port="3306", user=username,
                         passwd=password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY is ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
