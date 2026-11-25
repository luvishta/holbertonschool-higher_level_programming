#!/usr/bin/python3
"""module for selecting states where name is equal to the argument"""

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
    cursor.execute("SELECT * \
                    FROM `states` \
                    ORDER BY id")
    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)

    if cursor is not None:
        cursor.close()
    if database is not None:
        database.close()
