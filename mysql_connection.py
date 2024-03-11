import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='vans1',
                                host='localhost' , database='grocerry')

    return __cnx