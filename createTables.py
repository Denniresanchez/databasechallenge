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
    
    def createTables(): # function to create the tables
        cursor = conn.cursor()
        
        # create houses table
        cursor.execute(
            """CREATE TABLE houses (
			house_id int primary key NOT NULL,
			house_tag text NOT NULL,
			house_selling_price int,
            house_purchase_price int,
            house_spread int)"""
		)
        conn.commit()
        
    createTables()
        

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)