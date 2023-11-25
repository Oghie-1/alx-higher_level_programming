#!/usr/bin/python3
"""Displays all cities of a specified state"""
import MySQLdb
import sys


def list_cities():
    """Takes arguments argv to list from database
    Lists cities in the specified state

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
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

        state_name = sys.argv[4]
        cur.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = %s\
                    ORDER BY cities.id ASC", (state_name,))

        rows = cur.fetchall()

        city_names = [row[0] for row in rows]
        print(", ".join(city_names))

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if db:
            db.close()

if __name__ == "__main__":
    list_cities()
