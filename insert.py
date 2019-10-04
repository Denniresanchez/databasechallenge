import psycopg2

try:
    # required information to use the db 
    conn = psycopg2.connect(
        database = "investor", # database name
        user = "postgres",
        password = "6108", #your password
        host = "127.0.0.1",
        port = "5432"
    )
    
    def inserthouses(): # function to insert products
        cursor = conn.cursor()
        
        # insert products into database
        cursor.execute(
            """INSERT INTO houses (house_id, house_tag, house_selling_price, house_purchase_price, house_spread)
            VALUES (),
                (), 
                (),
                (),
                (),
                (),
                (),
                ()"""
		) 
        # not adding product details yet
        conn.commit()
        cursor.close()
        
    insertProducts()
        

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)