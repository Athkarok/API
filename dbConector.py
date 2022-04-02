from app import mysql

def query(cursor, sql, args):
    if not args:
        cursor.execute(sql)
    else:
        cursor.execute(sql, args)
    return cursor.fetchall()


def execute(sql, *args):

    cursor = mysql.connection.cursor()

    rows = query(cursor, sql, args)

    mysql.connection.commit()
    cursor.close()
    return rows

