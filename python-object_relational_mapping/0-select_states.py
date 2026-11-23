#!/usr/bin/python3
"""Module for the states that is selected"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = database.cursor()

    cursor.execute('SELECT * FROM states ')

    for state in cursor.fetchall():
        print(state)

    if cursor is not None:
        cursor.close()
    if database is not None:
        database.close()
