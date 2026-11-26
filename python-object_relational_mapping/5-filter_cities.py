#!/usr/bin/python3
"""module for selecting cities by state """

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
        'SELECT  cities.name ,states.name '
        'FROM cities '
        'INNER JOIN states ON states.id = cities.state_id '
    )
    cities = []
    for city in cursor.fetchall():
        if city[1] == argv[4]:
            cities.append(city[0])

    print(", ".join(cities))

    if cursor is not None:
        cursor.close()
    if database is not None:
        database.close()
