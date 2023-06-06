import mariadb
import dbcreds

def run_statement(sql, args=None):
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql,args)
        result = cursor.fetchall()
    except Exception as error:
        print("Exception:", error)
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.close()
        return result