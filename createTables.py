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
			house_id SERIAL NOT NULL PRIMARY KEY,
			house_location text NOT NULL,
            house_area text,
			house_selling_price int,
            house_purchase_price int,
            house_owner text)"""
		)
        conn.commit()

        cursor.execute(
            """CREATE TABLE transactions (
			house_id int primary key NOT NULL,
			house_selling_price int)"""
		)
        conn.commit()

        cursor.execute(
            """CREATE TABLE accounts (
			user_id SERIAL NOT NULL PRIMARY KEY,
            username text NOT NULL,
			user_pass text NOT NULL,
            user_class text)"""
		)
        conn.commit()

        cursor.close()

    createTables()
        

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data PostgreSQL", error)