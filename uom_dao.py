
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uno")
    cursor.execute(query)
    response = []
    for (uno_id, uno_name) in cursor:
        response.append({
            'uno_id': uno_id,
            'uno_name': uno_name
        })
    return response


if __name__ == '__main__':
    from mysql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))