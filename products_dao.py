from mysql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = "SELECT products.products_id,products.name,products.uno_id,products.price_per_unit,uno.uno_name FROM grocerry.products inner join uno on products.uno_id = uno.uno_id;"
    cursor.execute(query) 
    
    response= []

    for (product_id,name,uno_id,price_per_unit,uno_name) in cursor:
        response.append(
            {
                
                'product_id':product_id,
                'name':name,
                'uno_id' : uno_id,
                'price_per_unit':  price_per_unit , 
                'uno_name' : uno_name
                }
        )
                    
    
    return response

def insert_new_products(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uno_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uno_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid

def delete_product(connection, products_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where products_id=" + str(products_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid
    

if __name__ == '__main__' :
    connection = get_sql_connection()
    print(delete_product(connection,12))


