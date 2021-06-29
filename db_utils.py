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

def get_table(dbname, tablename, filter_dict= None):
        try:
            where_clause = " where "
            sql_string = f"select * from {tablename}"
            if filter_dict and len(filter_dict) > 0:
                item = filter_dict.items[0]
                sql_string += f"where {item[0]} = {item[1]}"
                if len(filter_dict) > 1:
                    # and ....additional query params
                    raise("Not implemented yet")

            my_query = query_db(dbname, sql_string)
            json_output = json.dumps(my_query)
        except Exception as e:
            raise('ERROR retrieving {table_name}')

        return json_output
