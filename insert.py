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
    
    # def inserthouses(): # function to insert products
    #     cursor = conn.cursor()
        
    #     # insert products into database
    #     cursor.execute(
    #         """INSERT INTO houses (house_location, house_area, house_purchase_price, house_selling_price, house_owner)
    #         VALUES ('Hialeah', '1450', 100000, 160000,'Juan'),
    #             ('Miami Beach', '1300', 400000, 460000, 'Carlos'), 
    #             ('downtonw Miami', '700', 350000, 410000, 'Alicia'),
    #             ('West Palm Beach', '1000', 460000, 500000, 'Pablo'),
    #             ('North Miami', '650', 13000, 25000,'Jason'),
    #             ('South beach','1750', 10000000, 15000000, 'Jose'),
    #             ('Hollywood', '765', 400000, 490000, 'Andres' ),
    #             ('Aventura', '900', 75000, 100000, 'Carla'),
    #             ('Hollywood', '800', 480000, 510000, 'Michael'),
    #             ('Aventura', '650', 230000, 350000, 'John')"""
	# 	) 
    #     # not adding product details yet
    #     conn.commit()
    #     cursor.close()
        
    # inserthouses()
    
    def insertaccounts(): # function to insert products
            cursor = conn.cursor()
            
            # insert products into database
            cursor.execute(
                """INSERT INTO accounts (username, user_pass)
                VALUES ('Dunieski','ilovemac'),
                ('Etzer', 'microsoft')"""
            ) 
            # not adding product details yet
            conn.commit()
            cursor.close()
            
    insertaccounts()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)