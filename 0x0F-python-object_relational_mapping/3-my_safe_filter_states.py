#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa
with a name starting with N"""

import MySQLdb
import sys

if __name__ == '__main__':

    """Connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    """Create a cursor object"""
    cur = db.cursor()

    input_name = sys.argv[4];

    """Grab all states in ascending order"""
    cur.execute("SELECT * FROM states WHERE name = %s;", (input_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print ('{}'.format(row))
