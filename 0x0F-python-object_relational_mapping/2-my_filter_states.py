#!/usr/bin/python3

"""Display name argument of states table"""
import MySQLdb
import sys


def filter_names():
    """Takes arguments argv to list from database
    Only lists states that match the provided name argument

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
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

        cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                    ORDER BY id ASC".format(sys.argv[4]))
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
    filter_names()
