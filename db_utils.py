import json
import sqlite3


def db(database_name):
    try:
        return sqlite3.connect(database_name)
    except:
        raise(f"Error connecting to {database_name}")

def query_db(db_name, query, args=(), one=False):
    cur = db(db_name).cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

def get_table(dbname, tablename):
        try:
            sql_string = f"select * from {tablename}"
            my_query = query_db(dbname, sql_string)
        except Exception as e:
            raise('ERROR retrieving {table_name}')
        return my_query
