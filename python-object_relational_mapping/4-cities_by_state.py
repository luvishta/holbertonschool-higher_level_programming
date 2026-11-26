#!/usr/bin/python3
"""module for selecting cities """

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

    cursor.execute(
        'SELECT cities.id, cities.name, states.name '
        'FROM cities '
        'INNER JOIN states ON states.id = cities.state_id '
        'ORDER BY cities.id ASC'
    )
    for state in cursor.fetchall():
        print(state)

    if cursor is not None:
        cursor.close()
    if database is not None:
        database.close()
