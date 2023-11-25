#!/usr/bin/python3
"""Script that lists all states with a name starting with N"""
import MySQLdb
import sys


def get_states_n():
    """Takes arguments argv to list from database
    Only lists states that start with N

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if db:
            db.close()

if __name__ == "__main__":
    get_states_n()
